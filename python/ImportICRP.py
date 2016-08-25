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
import re
import vtk

import showData as vis
import itkStats as ist
import vtkClip  as vc 

#----------------------------------------------
# Define variables
#
# columns, rows, slices
ConstPixelDims = (254, 127, 222)
ConstPixelSpacing = (2.137, 2.137, 8.0)
origin = (0,0,0)

dataDir = "/home/apr/Work/NPL/MRT2/Phantoms/P110 data V1.2/"
dataFile = "AM/AM.dat"
outputFile = "abc"
#----------------------------------------------

#----------------------------------------------
# Options:
#
innerContour   = -0.1    # Level to define volume after anti-aliasing (organs)
#innerContour   = -0.5    # Level to define volume after anti-aliasing (cube)
shellThickness =  2.0    # Shell thickness in voxels
aaConverge     = 0.00005 # MaximumRMSChange for anti-aliasing (smaller = tighter but slower)

relaxFactor      = 0.01 # Specify the relaxation factor for Laplacian smoothing. 
smoothIterations = 700  # Specifiy number of smoothing iterations

#debug = 0    # Don't show data
#debug = 1    # Show CT and VOI
#debug = 2    # Show final itk image
#debug = 3    # Show both
#showHist = 0 # Show the histogram for the anti-aliased data
#debugVol = 0 # Show the volume for each step of calculation
#noVis = 0 # Set variable to turn off visualing ISO su
#----------------------------------------------

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
#icrp3D[icrp3D != organ] = 0

# Show the raw icrp data
vis.arrayShow(icrp3D, 2)

# Create ITKimages from arrays
print 'Creating raw itk images...'
itkOrgan =sitk.GetImageFromArray(icrp3D)
print '\n[itkOrgan Info]'
ist.itkInfo(itkOrgan)

# Show the itk image
vis.itkShow(itkOrgan,2)


################################################################################################################################
################################
# This taken for DicomToSTL.py #
################################
################################################################################################################################

# Defoen what value corresposnds to inside the VOI
thresholdValue = organ

#---------------------------------------------------
# Maniuplate the itk images
print 'Manipulating itk images...'

# Use this for mouse model
#organSeeds=sitk.VectorUIntList([[172,184,ConstPixelDims[2]/2],[226,188,ConstPixelDims[2]/2]])
#organMask=sitk.ConnectedThreshold(itkOrgan,organSeeds,15300.0,20000.0,1)

# Use this for masked CT
organMask=sitk.BinaryThreshold(itkOrgan,1,thresholdValue,1,0)

organMask=sitk.BinaryClosingByReconstruction(organMask,30)

#organMask=sitk.BinaryDilate(organMask)

organMask=sitk.AntiAliasBinary(organMask,aaConverge) #Output from antialias filter is float64    

# Show the final histogram
vis.itkHist(organMask, "itkAA")

# Show the final itk image
vis.itkShow(organMask,2)
#---------------------------------------------------

#---------------------------------------------------
# Read the itk image into vtk
print "Creating vtk volume from itk image..."
dataImporter = vtk.vtkImageImport() 
data_string = sitk.GetArrayFromImage(organMask).tostring()
dataImporter.CopyImportVoidPointer(data_string, len(data_string))
dataImporter.SetDataScalarTypeToDouble()
dataImporter.SetNumberOfScalarComponents(1)
dataImporter.SetDataExtent(0,ConstPixelDims[2]-1,0,ConstPixelDims[1]-1,0,ConstPixelDims[0]-1)   # z y x
dataImporter.SetWholeExtent(0,ConstPixelDims[2]-1, 0,ConstPixelDims[1]-1,0,ConstPixelDims[0]-1) # z y x

dataImporter.Update()

# Create VTK Image volume and set origin and spacing
organVolume=dataImporter.GetOutput()  
organVolume.SetOrigin(origin[1], origin[1], origin[0])                                 # z y x
organVolume.SetSpacing(ConstPixelSpacing[2],ConstPixelSpacing[1],ConstPixelSpacing[0]) # z y x
#---------------------------------------------------

#---------------------------------------------------
# Extract isosurface using VTK marching cubes filter
outerContour = innerContour - shellThickness
print "Extracting iso surfaces from ", innerContour, " to ", outerContour
organMarch=vtk.vtkMarchingCubes()  
organMarch.SetInputData(organVolume)
organMarch.SetValue(0,outerContour)
organMarch.SetValue(1,innerContour)
organMarch.ComputeNormalsOn()
organMarch.ComputeScalarsOn()
organMarch.Update()
organPolys=organMarch.GetOutput()

print "Extracting inner contour = ", innerContour
organVolMarch=vtk.vtkMarchingCubes()  
organVolMarch.SetInputData(organVolume)
organVolMarch.SetValue(0,innerContour) # better for organs
organVolMarch.ComputeNormalsOn()
organVolMarch.ComputeScalarsOn()
organVolMarch.Update()
organVol=organVolMarch.GetOutput()
#--------------------------------------------------

#---------------------------------------------------
# Calculate the volume and surface area from isosurface
massVTK = vtk.vtkMassProperties()
massVTK.SetInputData(organVol)
massVTK.Update() 

volumeISO = massVTK.GetVolume() 
areaISO   = massVTK.GetSurfaceArea()
print 'volumeISO = ', volumeISO, ' areaISO = ', areaISO

massVTKshell = vtk.vtkMassProperties()
massVTKshell.SetInputData(organPolys)
massVTKshell.Update() 

volumeShell = massVTKshell.GetVolume()
areaShell   = massVTKshell.GetSurfaceArea()
print 'volumeShell = ', volumeShell, ' areaShell = ', areaShell
#---------------------------------------------------

#---------------------------------------------------
# Show iso surface
print "Rendering iso surface..."
vis.showIso(organPolys, 'Original Shell')
#---------------------------------------------------

#--------------------------------------------------
# Smooth the surfaces
print "Smoothing surfaces..."
smoothOrganPolys=vtk.vtkSmoothPolyDataFilter()
smoothOrganPolys.SetInputData(organPolys)
smoothOrganPolys.SetRelaxationFactor(relaxFactor)
smoothOrganPolys.SetNumberOfIterations(smoothIterations)
smoothOrganPolys.Update()
organPolysSmooth=smoothOrganPolys.GetOutput()

smoothOrganVol=vtk.vtkSmoothPolyDataFilter()
smoothOrganVol.SetInputData(organVol)
smoothOrganVol.SetRelaxationFactor(relaxFactor)
smoothOrganVol.SetNumberOfIterations(smoothIterations)
smoothOrganVol.Update()
organVolSmooth=smoothOrganVol.GetOutput()
#--------------------------------------------------

#---------------------------------------------------
# Calculate the volume and surface area from isosurface
massVTKSmooth = vtk.vtkMassProperties()
massVTKSmooth.SetInputData(organVolSmooth)
massVTKSmooth.Update() 

volumeISOsmooth = massVTKSmooth.GetVolume() 
areaISOsmooth   = massVTKSmooth.GetSurfaceArea()
print 'volumeISOsmooth = ', volumeISOsmooth, ' areaISOsmooth = ', areaISOsmooth

massVTKshellSmooth = vtk.vtkMassProperties()
massVTKshellSmooth.SetInputData(organPolysSmooth)
massVTKshellSmooth.Update() 

volumeShellsmooth = massVTKshellSmooth.GetVolume()
areaShellsmooth   = massVTKshellSmooth.GetSurfaceArea()
print 'volumeShellsmooth = ', volumeShellsmooth, ' areaShellsmooth = ', areaShellsmooth
#---------------------------------------------------

#---------------------------------------------------
# Show iso surface
print "Rendering smooth iso surface..."
vis.showIso(organPolysSmooth, 'Smoothed Shell')
#---------------------------------------------------

#---------------------------------------------------
# Write STL
print "Writing STL Shell..."
vc.writeSTL(organPolys, outputFile, '_shell.stl' )

print "Writing STL Shell (smoothed)..."
vc.writeSTL(organPolysSmooth, outputFile, '_shell_smoothed.stl' )

print "Writing STL solid inner volume..."
vc.writeSTL(organVol, outputFile, '_solid.stl' )

print "Writing STL solid inner volume (smoothed)..."
vc.writeSTL(organVolSmooth, outputFile, '_solid_smoothed.stl' )

#---------------------------------------------------

# #---------------------------------------------------
# # Output a report
# print " "
# print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
# print 'Processed DICOM folder: ', PathDicom
# print ' Dimensions = ', ConstPixelDims
# print ' Spacing    = ', ConstPixelSpacing , ' mm'
# print ' '
 
# if VOIfile:
#     print 'Using VOI file: ', VOIfile
#     print " "
#     print 'Anti-alias MaximumRMSChange = ', aaConverge
#     print 'Inner Contour   = ',  innerContour 
#     print 'Shell Thickness = ',  shellThickness , ' voxels'
#     print " "
#     print 'Smoothing parameters: ', relaxFactor, ' ', smoothIterations
#     print " "
#     print ' {} {:15.2f} {}'.format('VOI volume            = ',volumeVOI,'mm^3')
#     print ' {} {:15.2f} {}'.format('ISO volume            = ',volumeISO,'mm^3')
#     print ' {} {:15.2f} {}'.format('Diff                  = ',100.0*((volumeISO - volumeVOI)/volumeVOI), '%')
#     print ' {} {:15.2f} {}'.format('ISO volume (smoothed) = ',volumeISOsmooth,'mm^3')
#     print ' {} {:15.2f} {}'.format('Diff                  = ',100.0*((volumeISOsmooth - volumeVOI)/volumeVOI), '%')
#     print " "
#     print ' {} {:15.2f} {}'.format('ISO area              = ',areaISO, 'mm^2')
#     print ' {} {:15.2f} {}'.format('ISO area (smoothed)   = ',areaISOsmooth, 'mm^2')
# print " "
# print 'Output file: ' , outputFile
# print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
# print ' '
# #---------------------------------------------------


# Finished
endTime = time.time()
elapsed = endTime - startTime
print 'Finished: ', elapsed, ' seconds.'


