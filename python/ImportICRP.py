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

vis.arrayShow(data3D, 2)

# Create ITKimages from arrays
print 'Creating raw itk images...'
itkCT =sitk.GetImageFromArray(data3D)
print '\n[itkCT Info]'
ist.itkInfo(itkCT)

vis.itkShow(itkCT,2)



# TODO: Pick whcih organs you want in the image from the lookup table
