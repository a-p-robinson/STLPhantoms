#################################################################################
# readICRP.py                                                                   #
#                                                                               #
# APR: 23/08/16                                                                 #
#                                                                               #
# Import the ICRP phantom data from ICRP Adult computational reference phantoms #
# http://www.icrp.org/publication.asp?id=ICRP%20Publication%20110               #
#                                                                               #
# http://www.icrp.org/docs/V1.2.zip                                             #
#                                                                               #
#    Copyright (C) 2016 Andrew Robinson                                         #
#                                                                               #
#    This program is free software: you can redistribute it and/or modify       #
#    it under the terms of the GNU General Public License as published by       #
#    the Free Software Foundation, either version 3 of the License, or          #
#    (at your option) any later version.                                        #
#                                                                               #
#    This program is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#    GNU General Public License for more details.                               #
#                                                                               #
#    You should have received a copy of the GNU General Public License          #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                               #
#################################################################################

import numpy as np
import SimpleITK as sitk
import re
import sys

import itkStats as ist

class readICRP:

    # Initialisation:
    #
    # Options:
    #   dataDir = path to ICRP phantom data
    #   model = male/female
    #   organ = all or name of organ ie, 'spleen'
    #
    def __init__(self, dataDir, model):

        # Define the input based on what the user has requested
        self.dataDir = dataDir
        
        if model == 'male':
            self.mod = 'AM'
            self.ConstPixelDims = (254, 127, 222)
            self.ConstPixelSpacing = (2.137, 2.137, 8.0)
            self.origin = (0,0,0)

        elif model == 'female':
            self.mod = 'AF'
            self.ConstPixelDims = (299, 137, 348)
            self.ConstPixelSpacing = (1.755, 1.755, 4.84)
            self.origin = (0,0,0)
        else:
              print >> sys.stderr, "Unknown model: " + model
              sys.exit(1)
              
        self.dataFile =  dataDir + '/' + self.mod + '/' + self.mod + '.dat'
        self.organFile =  dataDir + '/' + self.mod + '/' + self.mod + '_organs.dat'

        # Read in data
        self.icrpData = np.fromfile(self.dataFile, sep=" ")
        nPixelsOrgans = np.count_nonzero(self.icrpData)
        print "Read in ", nPixelsOrgans, " voxels from ", self.dataFile

        # Read in the organ file file
        with open(self.organFile, "r") as file:

            self.organID = []
            self.organName = []
            self.organTissueID = []
            self.organDensity = []
    
            # File header
            info_lines = []
            for line in range(0,4):
                info_lines.append(file.readline())

            # File contents
            for line in file.readlines():
                line = line.rstrip('\n\r')
                words = re.split(" *", line)
                self.organID.append(int(words[0]))
                self.organTissueID.append(int(words[-2]))
                self.organDensity.append(float(words[-1]))
                self.organName.append(re.sub('[,()]', '', ("_".join(words[1:-2])) ).lower())

    # Show the organs which are available in the model
    def listOrgans(self):
        print '---------------------------------'
        print 'ICRP 110 Refernce Phantom [' + self.mod + ']'
        print '---------------------------------'
        for i, val in enumerate(self.organName):
            print ' {} {:4.0f} {} {}'.format('organID:',self.organID[i],'name:',val)            
        print '---------------------------------'
        
    # Get the data and return itk image
    # option: organ = a list of organs you want to include in the image mask
    # option: value = value to set included voxels to (ignored if negative)
    def getData(self, organ=['all'], value=-99):
        
        # Create a local copy of the data
        icrp3D = np.copy(self.icrpData)
        # Reshape into 3D
        icrp3D = icrp3D.reshape(self.ConstPixelDims, order='F')
                
        # Pick the organs we want to use        
        foundOrgan = 0;
        organThreshold = []
        if organ[0] != 'all':
            
            for i, val in enumerate(self.organName):
                if val in organ:
                    organThreshold.append(self.organID[i]) 
                    print "Selecting " + val
                    foundOrgan = 1
                    
            if foundOrgan == 0:
                print >> sys.stderr, "Organ not found: ".join(organ)
                sys.exit(1)
            else:
                # Mask local data based on the requested organs
                final = np.copy(icrp3D)
                final.fill(0)
                for val in organThreshold:
                    # Copy the data
                    tmp1 = np.copy(icrp3D)
                    # Mask the temp copy
                    tmp1[icrp3D != val] = 0
                    # Add temp array to final
                    final = np.add(final,tmp1)

                # Set the included values to value if provided
                if value > 0:
                    final[final !=0] = value
                    
        # Create ITKimages from arrays
        print 'Creating raw itk images...'
        itkOrgan =sitk.GetImageFromArray(final)
        print '\n[itkOrgan Info]'
        ist.itkInfo(itkOrgan)

        # Return the image and threshold value (value of the non-zero voxels)
        return itkOrgan, organThreshold
