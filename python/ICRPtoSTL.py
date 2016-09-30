###############################################################################
# ICRPtoSTL.py                                                                #
# Convert the ICRP phantom data to STL files.                                 #
#                                                                             #
# APR: 25/08/16                                                               #
#                                                                             #
#    Copyright (C) 2016 Andrew Robinson                                       #
#                                                                             #
#    This program is free software: you can redistribute it and/or modify     #
#    it under the terms of the GNU General Public License as published by     #
#    the Free Software Foundation, either version 3 of the License, or        #
#    (at your option) any later version.                                      #
#                                                                             #
#    This program is distributed in the hope that it will be useful,          #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#    GNU General Public License for more details.                             #
#                                                                             #
#    You should have received a copy of the GNU General Public License        #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.    #
#                                                                             #
###############################################################################

import time
import argparse

import readICRP as icrp  # Reads in the ICRP phantom and retuen an itk image
import showData as vis   # Show slices of itk data
import dicomToSTL as dts # Conert an itk image to STL file

# Start timer
startTime = time.time()

# Print GPL license header
print "ICRPtoSTL  Copyright (C) 2016 Andrew Robinson"
print "This program comes with ABSOLUTELY NO WARRANTY"
print "This is free software, and you are welcome to redistribute it"
print "under certain conditions. Please see LICENSE.TXT for details."
print " "

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


