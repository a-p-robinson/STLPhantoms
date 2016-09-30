#################################################################################
# ICRPtoSTL.py                                                                  #
#                                                                               #
# APR: 25/08/16                                                                 #
#                                                                               #
# Convert the ICRP phantom data to STL files.                                   #
#################################################################################
                                                             
import time
import argparse

import readICRP as icrp  # Reads in the ICRP phantom and retuen an itk image
import showData as vis   # Show slices of itk data
import dicomToSTL as dts # Conert an itk image to STL file

# Start timer
startTime = time.time()

#---------------------------------------------------
# Define the arguments we want
parser = argparse.ArgumentParser()
parser.add_argument("model", help="Model to use (male or female)")
parser.add_argument("organ", help="Organ to process")

args = parser.parse_args()
model = args.model
organs = [item for item in args.organ.split(',')]
outFileName = model + '_' + '_'.join(organs)

print 'Will use model: ' + model
print 'Will include: '
print organs
#---------------------------------------------------

#-----------------------------------------
# Variables:
dataDir = "/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/" # Location of directory with ICRP data
debug = 0
#-----------------------------------------

# read in the ICRP data
data = icrp.readICRP(dataDir,model)

# # List the organs which are available
# data.listOrgans()

# Get the organ dat as an itk image
itkImage, organThreshold = data.getData(organs, 100)

if debug == 1:
    # Show the itk image
    vis.itkShow(itkImage,2)

# Convert the itk data to stl
abc = dts.dicomSTL(itkImage, data.ConstPixelDims, data.ConstPixelSpacing, data.origin, 100, outFileName)
abc.doAllTheThings()

# Finished
endTime = time.time()
elapsed = endTime - startTime
print 'Finished: ', elapsed, ' seconds.'


