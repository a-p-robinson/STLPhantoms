################################################################################
# ImportICRP.py                                                                #
#                                                                              #
# APR: 23/08/16                                                                #
#                                                                              #
# Import the ICRP phantom data from ICRP Adult computational refernce phantoms #
# http://www.icrp.org/publication.asp?id=ICRP%20Publication%20110              #
#                                                                              #
# http://www.icrp.org/docs/V1.2.zip                                            #
################################################################################

import numpy as np
import SimpleITK as sitk
import re

import showData as vis
import itkStats as ist

# rows, colums, slices
#ConstPixelDims = (127, 254, 222)
ConstPixelDims = (254, 127, 222)

data = np.fromfile("/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/AM/AM.dat", sep=" ")
data3D = data.reshape(ConstPixelDims, order='F')



print data
print data.size

print data3D
print data3D.size
nPixelsOrgans = np.count_nonzero(data3D)
print nPixelsOrgans

# Read in the orgna file file
organ_dictionary  = {} # Internally used dictionary

with open("/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/AM/AM_organs.dat", "r") as file:

    organID = []
    organName = []
    organTissueID = []
    organDensity = []
    
    # File header
    info_lines = []
    for line in range(0,4):
        info_lines.append(file.readline())
        
    for line in file.readlines():
        line = line.rstrip('\n\r')
        words = re.split(" *", line)
        organID.append(int(words[0]))
        organTissueID.append(int(words[-2]))
        organDensity.append(float(words[-1]))
        organName.append(re.sub('[,()]', '', ("_".join(words[1:-2])) ).lower())

print organID
print organName;
print organTissueID
print organDensity
        
# Pick organ
for i, val in enumerate(organName):
    if val == 'spleen':
        organ = organID[i] 
print organ
data3D[data3D != organ] = 0

vis.arrayShow(data3D, 2)

# Create ITKimages from arrays
print 'Creating raw itk images...'
itkCT =sitk.GetImageFromArray(data3D)
print '\n[itkCT Info]'
ist.itkInfo(itkCT)

vis.itkShow(itkCT,2)



# TODO: Pick whcih organs you want in the image from the lookup table
