#################################################################################
# readICRP.py                                                                   #
#                                                                               #
# APR: 23/08/16                                                                 #
#                                                                               #
# Import the ICRP phantom data from ICRP Adult computational reference phantoms #
# http://www.icrp.org/publication.asp?id=ICRP%20Publication%20110               #
#                                                                               #
# http://www.icrp.org/docs/V1.2.zip                                             #
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
    def __init__(self, dataDir, model, organ='all'):

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

        self.organName = organ

    # Get the data and return itk image
    def getData(self):
        
        # Read in data
        icrpData = np.fromfile(self.dataFile, sep=" ")
        icrp3D = icrpData.reshape(self.ConstPixelDims, order='F')
        nPixelsOrgans = np.count_nonzero(icrp3D)
        print "Read in ", nPixelsOrgans, " voxels from ", self.dataFile

        # Read in the organ file file
        with open(self.organFile, "r") as file:

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
        if self.organName != 'all':
            for i, val in enumerate(organName):
                if val == self.organName:
                    organThreshold = organID[i] 
                    print "Selecting " + self.organName
                    # Mask based on that organ
                    icrp3D[icrp3D != organThreshold] = 0
                    foundOrgan = 1
            if foundOrgan != 1:
                print >> sys.stderr, "Organ not found: " + self.organName
                sys.exit(1)
                 
        # Create ITKimages from arrays
        print 'Creating raw itk images...'
        itkOrgan =sitk.GetImageFromArray(icrp3D)
        print '\n[itkOrgan Info]'
        ist.itkInfo(itkOrgan)

        # Return the image and threshold
        return itkOrgan, organThreshold
