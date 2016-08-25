################################################################################
# dicomToSTL.py                                                                ~
#                                                                              #
# APR: 23/08/16                                                                #
#                                                                              #
# Module to convert an itk 3D image to STL file                                #
################################################################################

import numpy as np
import SimpleITK as sitk
import re
import vtk

import showData as vis
import itkStats as ist
import vtkClip  as vc 

class dicomSTL:

    # Initilisation:
    # Options: 
    def __init__(self, itkImage, PixelDims, PixelSpacing, ImageOrigin, threshold, outputFilePath):

        self.itkI              = itkImage       # The image that we want to work with
        self.outputFile        = outputFilePath # Common part of oputput file path

        self.ConstPixelDims    = PixelDims      # Number of Pixels
        self.ConstPixelSpacing = PixelSpacing   # Voxel sizes (mm)
        self.origin            = ImageOrigin    # Center of the image (mm)

        self.thresholdValue    = threshold      # Define what value corresposnds to inside the VOI
        
    def doAllTheThings(self):
        
        #----------------------------------------------
        # Options:
        #
        innerContour   = -0.1    # Level to define volume after anti-aliasing (organs)
        #innerContour   = -0.5    # Level to define volume after anti-aliasing (cube)
        shellThickness =  2.0    # Shell thickness in voxels
        aaConverge     = 0.00005 # MaximumRMSChange for anti-aliasing (smaller = tighter but slower)
        
        relaxFactor      = 0.01 # Specify the relaxation factor for Laplacian smoothing. 
        smoothIterations = 700  # Specifiy number of smoothing iterations
        #----------------------------------------------

        #---------------------------------------------------
        # Maniuplate the itk images
        print 'Manipulating itk images...'
        
        # Use this for masked CT
        organMask=sitk.BinaryThreshold(self.itkI,1,self.thresholdValue,1,0)
        
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
        dataImporter.SetDataExtent(0,self.ConstPixelDims[2]-1,0,self.ConstPixelDims[1]-1,0,self.ConstPixelDims[0]-1)   # z y x
        dataImporter.SetWholeExtent(0,self.ConstPixelDims[2]-1, 0,self.ConstPixelDims[1]-1,0,self.ConstPixelDims[0]-1) # z y x
        
        dataImporter.Update()

        # Create VTK Image volume and set origin and spacing
        organVolume=dataImporter.GetOutput()  
        organVolume.SetOrigin(self.origin[1], self.origin[1], self.origin[0])                                 # z y x
        organVolume.SetSpacing(self.ConstPixelSpacing[2],self.ConstPixelSpacing[1],self.ConstPixelSpacing[0]) # z y x
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
        vc.writeSTL(organPolys, self.outputFile, '_shell.stl' )
        
        print "Writing STL Shell (smoothed)..."
        vc.writeSTL(organPolysSmooth, self.outputFile, '_shell_smoothed.stl' )
        
        print "Writing STL solid inner volume..."
        vc.writeSTL(organVol, self.outputFile, '_solid.stl' )
        
        print "Writing STL solid inner volume (smoothed)..."
        vc.writeSTL(organVolSmooth, self.outputFile, '_solid_smoothed.stl' )
        
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




