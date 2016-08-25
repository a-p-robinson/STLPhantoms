################################################################################
# readICRP.py                                                                  #
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
import sys

class readICRP:

    # Initilisation:
    #
    # Options:
    #   dataDir = path to ICRP phatnom data
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

        elif: model == 'female':
            self.mod = 'AF'
            self.ConstPixelDims = (254, 127, 222)
            self.ConstPixelSpacing = (2.137, 2.137, 8.0)
            self.origin = (0,0,0)
        else:
              print >> sys.stderr, "Something is seriously wrong."
              sys.exit(1)
              
        self.dataFile =  dataDir + '/' + self.model + ' /' + self.model + '.dat'
        self.organFile =  dataDir + '/' + self.model + ' /' + self.model + '_organs.dat'

        self.organName = organ
        
        # Read in data
        icrpData = np.fromfile(seld.dataFile, sep=" ")
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
                    organ = organID[i] 
                    print "Selecting " + self.organName
                    # Mask based on that organ
                    icrp3D[icrp3D != self.organName] = 0
                else:
                    print >> sys.stderr, "Something is seriously wrong."
                    sys.exit(1)
                 

        # Show the raw icrp data
        vis.arrayShow(icrp3D, 2)

        # Create ITKimages from arrays
        print 'Creating raw itk images...'
        itkOrgan =sitk.GetImageFromArray(icrp3D)
        print '\n[itkOrgan Info]'
        ist.itkInfo(itkOrgan)

        # Returen the image and pixel dimensions and threshold
        
