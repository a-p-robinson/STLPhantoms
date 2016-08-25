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
import time
import SimpleITK as sitk
import re
import vtk

import showData as vis
import itkStats as ist

import dicomToSTL as dts

# Start timer
startTime = time.time()

dataDir = "/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/"
dataFile = "AM/AM.dat"
ConstPixelDims = (254, 127, 222)
ConstPixelSpacing = (2.137, 2.137, 8.0)
origin = (0,0,0)


# Read in data
icrpData = np.fromfile(dataDir+dataFile, sep=" ")
icrp3D = icrpData.reshape(ConstPixelDims, order='F')
nPixelsOrgans = np.count_nonzero(icrp3D)
print "Read in ", nPixelsOrgans, " voxels from ", dataDir+dataFile

# Read in the organ file file
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
        
# Pick the organ we want to use 
for i, val in enumerate(organName):
    if val == 'spleen':
        organ = organID[i] 
print organ

# Mask based on that organ
icrp3D[icrp3D != organ] = 0

# Show the raw icrp data
#vis.arrayShow(icrp3D, 2)

# Create ITKimages from arrays
print 'Creating raw itk images...'
itkOrgan =sitk.GetImageFromArray(icrp3D)
print '\n[itkOrgan Info]'
ist.itkInfo(itkOrgan)

# Show the itk image
#vis.itkShow(itkOrgan,2)

abc = dts.dicomSTL(itkOrgan, ConstPixelDims, ConstPixelSpacing, origin, organ, '/home/apr/Work/NPL/MRT2/Phantoms/test')
abc.doAllTheThings()

# Finished
endTime = time.time()
elapsed = endTime - startTime
print 'Finished: ', elapsed, ' seconds.'


