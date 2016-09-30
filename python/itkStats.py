###############################################################################
# itkStats.py                                                                 #
# Functions to check itk image stats                                          #
#                                                                             #
# APR: 18/11/15                                                               #
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

import SimpleITK as sitk

#-----------------------------
# Print out information on an itk image
def itkInfo(img):

    stats = sitk.StatisticsImageFilter()
    stats.Execute(img)

    print 'Image Details:'
    print ' nDimensions = ', img.GetDimension()
    print ' Size        = ', img.GetSize()
    print '   Depth     = ', img.GetDepth()
    print '   Height    =', img.GetHeight()
    print '   Width     = ', img.GetWidth()
    print ' Pixel Type  = ', img.GetPixelIDTypeAsString()
    #print img.GetPixelIDValue()
    print 'Statistics:'
    print ' Min       = ', stats.GetMinimum()
    print ' Max       = ', stats.GetMaximum()
    print ' Mean      = ', stats.GetMean()
    print ' Sum       = ', stats.GetSum()
    print ' Sigma     = ', stats.GetSigma()
    print ' Variance  = ', stats.GetVariance()
#-----------------------------

#-----------------------------
# Get the number of non-zero pixels in itk image
def itkNonZero(img, testVal = 0.0):

    nz = 0
    w = img.GetWidth()
    h = img.GetHeight()
    d = img.GetDepth()

    for i in range(0, w):
        for j in range(0, h):
            for k in range(0, d):
                p = img.GetPixel(i,j,k)
                if p != testVal:
                    nz = nz + 1
                    print '[{},{},{}] {}'.format(i,j,k,p)

    return nz
#-----------------------------
