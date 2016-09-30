###############################################################################
# vtkClip.py                                                                  #
# Functions to clip a vtk poly object along a plane and return the two halves #
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

import vtk

# Cut a poly object through the center of mass and return both parts
def planeCut(polys):

    # Get the enter of mass of the shell 
    comVTK = vtk.vtkCenterOfMass()
    comVTK.SetInputData(polys)
    comVTK.Update()
    com = comVTK.GetCenter()

    # Define a plane
    plane = vtk.vtkPlane()
    plane.SetOrigin(com)
    plane.SetNormal(0,0,1)

    # Define a plane collection (used by clipclosedsurface)
    planeS = vtk.vtkPlaneCollection()
    planeS.AddItem(plane)

    #Setup cut - this does not close the surfaces (makes hollow)
    clip = vtk.vtkClipPolyData()
    clip.SetClipFunction(plane)
    clip.SetInputData(polys)
    clip.GenerateClippedOutputOn()
    clip.Update()
    clipped1 = clip.GetOutput()
    clipped2 = clip.GetClippedOutput()

    # # Cut and close the surface (this caps the whole volume !)
    # # Alos needs to be done for each half
    # clip = vtk.vtkClipClosedSurface()
    # clip.SetClippingPlanes(planeS)
    # clip.SetInputData(polys)
    # clip.GenerateOutlineOn()
    # clip.Update()
    # clipped1 = clip.GetOutput()
    # clipped2 = clip.GetOutput()

    # # Using cutter (3D - 2D) to get the lines so we can fill in
    # cut = vtk.vtkCutter()

    # cut.SetCutFunction(plane)
    # cut.SetInputData(polys) 
    # cut.Update()
    # cut1 = cut.GetOutput()

    # strip = vtk.vtkStripper()
    # strip.SetInputData(cut1)
    # strip.Update()
    # s = strip.GetOutput()

    # # Use a ruled surface filer to fill in the ends
    # rs = vtk.vtkRuledSurfaceFilter()
    # rs.SetInputData(s)
    # rs.CloseSurfaceOn()
    # rs.Update()
    # end = rs.GetOutput()

    # clipped1 = end
    # clipped2 = end

    # # We need to make these solid now
    # bcf = vtk.vtkBandedPolyDataContourFilter()
    # bcf.SetInputData(clipped1)
    # bcf.GenerateValues(10, -0.1, 2.0)
    # bcf.SetScalarModeToIndex()
    # bcf.GenerateContourEdgesOff()
    # bcf.Update()
    # bcf1 = bcf.GetOutput()

    return clipped1, clipped2

# Write the STL file
def writeSTL(polys, filename, extension):

    tmpFile = filename + extension
    organWriter=vtk.vtkSTLWriter()
    organWriter.SetFileName(tmpFile)
    organWriter.SetInputData(polys)
    organWriter.Write()

    print "Written STL Shell [", tmpFile, "]"
