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

import readICRP as icrp
import dicomToSTL as dts

# Start timer
startTime = time.time()

dataDir = "/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/"

data = icrp.readICRP(dataDir,'male','spleen')
#itkOrgan, ConstPixelDims, ConstPixelSpacing, origin, organThrehold = data.getData()
itkOrgan, organThreshold = data.getData()

# Show the itk image
vis.itkShow(itkOrgan,2)

abc = dts.dicomSTL(itkOrgan, data.ConstPixelDims, data.ConstPixelSpacing, data.origin, organThreshold, '/home/apr/Work/NPL/MRT2/Phantoms/test')
abc.doAllTheThings()

# Finished
endTime = time.time()
elapsed = endTime - startTime
print 'Finished: ', elapsed, ' seconds.'


