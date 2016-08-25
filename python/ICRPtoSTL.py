#################################################################################
# ICRPtoSTL.py                                                                  #
#                                                                               #
# APR: 25/08/16                                                                 #
#                                                                               #
# Convert the ICRP phantom data to STL files.                                   #
#################################################################################
                                                             
import time

import readICRP as icrp  # Reads in the ICRP phantom and retuen an itk image
import showData as vis   # Show slices of itk data
import dicomToSTL as dts # Conert an itk iamge to STL file

# Start timer
startTime = time.time()

#-----------------------------------------
# Variables:
dataDir = "/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/" # Location of directory with ICRP data
#-----------------------------------------

# read in the ICRP data
data = icrp.readICRP(dataDir,'male','spleen')
itkImage, organThreshold = data.getData()

# Show the itk image
vis.itkShow(itkImage,2)

# Convert the itk data to stl
abc = dts.dicomSTL(itkImage, data.ConstPixelDims, data.ConstPixelSpacing, data.origin, organThreshold, '/home/apr/Work/NPL/MRT2/Phantoms/test')
abc.doAllTheThings()

# Finished
endTime = time.time()
elapsed = endTime - startTime
print 'Finished: ', elapsed, ' seconds.'


