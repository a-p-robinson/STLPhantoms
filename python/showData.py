################################
# showData.py                  #
#                              #
# APR: 17/11/15                #
#                              #
# Functions to show image data #
################################

import sys
import numpy 

from matplotlib import colors
import matplotlib.pyplot as plt

import SimpleITK as sitk
import vtk

#---------------------------------------------------
# Loop through array and show each slice
def arrayShow(img, dim):

    # Create Plot
    plt.ion()
    f = plt.figure()
    ax = f.gca()
    annotate = None

    sys.stdout.write('Array Slice: ')
    sys.stdout.flush()
    # Loop through slices
    for i in range(0,img.shape[dim]):

        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()

        # Get the correct 2D image
        if dim == 0:
            image = img[i,:,:]
        if dim == 1:
            image = img[:,i,:]
        if dim == 2:
            image = img[:,:,i]

        # Get statistics on the image slice
        min  = numpy.amin(image)
        max  = numpy.amax(image)
        mean = numpy.max(image)
        
        # Clear previous plots and annotations
        ax.cla()
        if annotate:
            annotate.set_visible(False)
            del annotate

        # Draw the new image
        p = ax.imshow(image, cmap='gray')
        titleText = '(dim: {}) - slice {}'.format(dim,i)
        ax.set_title(titleText)
        plt.axis([0,image.shape[1],image.shape[0],0])
        annotate = f.text(0.25, 0.80, '{} {}\n{} {}\n{} {}'.format('Min:',min,'Max:',max,'Mean:',mean), va='center', fontsize=14, color='red')
        f.canvas.draw()

    # Close the figure when we are done with it
    plt.close()
    print " "
#---------------------------------------------------

#---------------------------------------------------
# Loop through array and mask and show each slice
def arrayShowTwo(img1, img2, dim, overlap=False):

    # Create Plot
    plt.ion()
    if overlap:
        f , ax = plt.subplots(1,1, dpi=120)
    else:
        f , ax = plt.subplots(1,2, dpi=120)

    annotate = None
    annotate2 = None

    sys.stdout.write('Array Slice: ')
    sys.stdout.flush()
    # Loop through slices
    for i in range(0,img1.shape[dim]):

        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()

        # Get the correct 2D image
        if dim == 0:
            image1 = img1[i,:,:]
            image2 = img2[i,:,:]
        if dim == 1:
            image1 = img1[:,i,:]
            image2 = img2[:,i,:]
        if dim == 2:
            image1 = img1[:,:,i]
            image2 = img2[:,:,i]

        # Get statistics on the image slice
        min1  = numpy.amin(image1)
        max1  = numpy.amax(image1)
        mean1 = numpy.max(image1)

        min2  = numpy.amin(image2)
        max2  = numpy.amax(image2)
        mean2 = numpy.max(image2)
        
        # Clear previous plots and annotations
        if overlap: 
            ax.cla()
        else:
            ax[0].cla()
            ax[1].cla()

        if annotate:
            annotate.set_visible(False)
            del annotate
        if annotate2:
            annotate2.set_visible(False)
            del annotate2

        # Draw the new image
        titleText = '(dim: {}) - slice {}'.format(dim,i)
        cmap = colors.ListedColormap(['black', 'green'])

        if overlap:
            p  = ax.imshow(image1, cmap='gray')
            p2 = ax.imshow(image2, cmap=cmap, alpha=0.5)
            ax.set_title(titleText)
            plt.axis([0,image1.shape[1],image1.shape[0],0])        
            annotate = f.text(0.25, 0.82, '{} {}\n{} {}\n{} {}'.format('Min:',min1,'Max:',max1,'Mean:',mean1), va='center', fontsize=14, color='red')
        else:
            p = ax[0].imshow(image1, cmap='gray')
            ax[0].set_title(titleText)
            plt.axis([0,image1.shape[1],image1.shape[0],0])        
            annotate = f.text(0.25, 0.85, '{} {}\n{} {}\n{} {}'.format('Min:',min1,'Max:',max1,'Mean:',mean1), va='center', fontsize=14, color='red')

            p2 = ax[1].imshow(image2, cmap=cmap)
            ax[1].set_title(titleText)
            plt.axis([0,image2.shape[1],image2.shape[0],0])
            annotate2 = f.text(0.67, 0.85, '{} {}\n{} {}\n{} {}'.format('Min:',min2,'Max:',max2,'Mean:',mean2), va='center', fontsize=14, color='green')

        f.canvas.draw()

    # Close the figure when we are done with it
    plt.close()
    print " "
#---------------------------------------------------

#-----------------------------
# Show all slices of an itk image
def itkShow(img, dim):

    # Create Plot
    plt.ion()
    f = plt.figure()
    ax = f.gca()
    annotate = None
    first = -1
    sys.stdout.write('itk Slice: ')
    sys.stdout.flush()

    # Calcualte loop and vindex
    size = img.GetSize()
    ind = (img.GetDimension() - 1) - dim

    # Loop through slices
    for i in range(0,size[ind]):

        sys.stdout.write(str(i) + ' ')
        sys.stdout.flush()

        # Get the correct 2D image
        if dim == 0:
            image = sitk.GetArrayFromImage(img)[i,:,:]
        if dim == 1:
            image = sitk.GetArrayFromImage(img)[:,i,:]
        if dim == 2:
            image = sitk.GetArrayFromImage(img)[:,:,i]

        # Get statistics on the image
        min  = numpy.amin(image)
        max  = numpy.amax(image)
        mean = numpy.max(image)
        
        # Check that we have some data on the slice
        if max != min:

            # Record the slices displayed
            if first < 0:
                first = i
            last = i

            # Clear previous plots and annotations
            ax.cla()
            if annotate:
                annotate.set_visible(False)
                del annotate

            # Draw the new image
            p = ax.imshow(image, cmap='gray')
            titleText = 'CT (dim: {}) - slice {}'.format(dim,i)
            ax.set_title(titleText)
            plt.axis([0,image.shape[1],image.shape[0],0])
            annotate = f.text(0.25, 0.80, '{} {}\n{} {}\n{} {}\n{} {} to {}'.format('Min:',min,'Max:',max,'Mean:',mean,'Showing slices: ',first,last), va='center', fontsize=14, color='red')
            f.canvas.draw()

    # Close the figure when we are done with it
    plt.close()
    print " "
#-----------------------------


#-----------------------------
# Plot the histogram of values in an itk image 
def itkHist(data,title, nbins = 1000, log = True):
    plt.ioff()
    d = sitk.GetArrayFromImage(data)

    hist=numpy.histogram(d,bins=nbins)

    plt.plot(hist[1][1:],hist[0])

    if log:
        plt.yscale('log')
    plt.title(title)
    plt.show()
#-----------------------------


#---------------------------------------------------
# Render iso surface
def showIso(data, name='Render'):
    organMapper=vtk.vtkPolyDataMapper()   #Render the extracted organ surface
    organMapper.ScalarVisibilityOff()
    organMapper.SetInputData(data)
    organProperty = vtk.vtkProperty()
    organProperty.SetColor(0.9,0.8,0.6)
    organProperty.SetInterpolationToGouraud()
    organProperty.BackfaceCullingOn()
    organProperty.SetOpacity(0.7)
    organActor = vtk.vtkActor()
    organActor.SetMapper(organMapper)
    organActor.SetProperty(organProperty)

    renderer = vtk.vtkRenderer()
    renderWin = vtk.vtkRenderWindow()
    renderWin.AddRenderer(renderer)
    renderInteractor = vtk.vtkRenderWindowInteractor()
    renderInteractor.SetRenderWindow(renderWin)
    renderer.AddActor(organActor)
    renderer.SetBackground(1,1,1)
    renderWin.SetSize(400, 400)
    #renderWin.AddObserver("AbortCheckEvent", CheckAbort)
    renderInteractor.Initialize()
    renderWin.Render()
    renderWin.SetWindowName(name)
    renderInteractor.Start()
#---------------------------------------------------
