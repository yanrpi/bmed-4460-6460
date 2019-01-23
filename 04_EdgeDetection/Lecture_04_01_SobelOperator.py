import SimpleITK as sitk
print(sitk.Version())

# import numpy as np
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':

    # %%
    
    print("Lecture 04")
    
    img_file_name = "GFP_06-DAPI.tif"
    print("... reading image from file: " + img_file_name)
    
    # %%
    
    '''Convert image to array and use matplotlib '''
    itkImage = sitk.ReadImage(img_file_name)
    print('Image has been loaded.')
    print('*'*40)
    print(itkImage)
    numpyArray = sitk.GetArrayFromImage(itkImage)
    plt.imshow(numpyArray, cmap='gray')
    plt.show()

    # %%

    itkImage = sitk.Cast(itkImage, sitk.sitkFloat32)
    grad_filter = sitk.GradientImageFilter()
    grad = grad_filter.Execute(itkImage)
    arr = sitk.GetArrayFromImage(grad)
    grad_mag = np.sum(arr**2, axis=2)
    plt.subplot(1,2,1)
    plt.imshow(numpyArray, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(grad_mag, cmap='gray')
    plt.title('Gradient Image')
    plt.show()
    
    # %%

    itkImage = sitk.Cast(itkImage, sitk.sitkFloat32)
    smoothed_image = sitk.SmoothingRecursiveGaussian(itkImage,4.0)
    #fNameOut =  'SmoothingRecursiveGaussian.tif'
    #sitk.WriteImage(sitk.Cast(smooth, sitk.sitkUInt8), fNameOut)
    plt.subplot(1,2,1)
    plt.imshow(numpyArray, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(sitk.GetArrayFromImage(smoothed_image), cmap='gray')
    plt.title('Smoothed Image')
    plt.show()

# Compute gradient after smoothing
    grad = grad_filter.Execute(smoothed_image)
    arr = sitk.GetArrayFromImage(grad)
    smoothed_grad_mag = np.sum(arr**2, axis=2)
    plt.subplot(1,3,1)
    plt.imshow(numpyArray, cmap='gray')
    plt.subplot(1,3,2)
    plt.imshow(grad_mag, cmap='gray')
    plt.title('Gradient wo smooth')
    plt.subplot(1,3,3)
    plt.imshow(smoothed_grad_mag, cmap='gray')
    plt.title('Smoothed Gradient')
    plt.show()

    # %%
    
    sobelImage = sitk.SobelEdgeDetection(itkImage)
    #fNameOut =  'SobelEdgeDetection.tif'
    #sitk.WriteImage(sitk.Cast(sobelImage, sitk.sitkUInt8), fNameOut)   
    plt.subplot(1,2,1)
    plt.imshow(numpyArray, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(  sitk.GetArrayFromImage(sobelImage), cmap='gray'  )
    plt.title('Sobel Edge Detection')
    plt.show()

    # %%

    sobelImageSmooth = sitk.SobelEdgeDetection(smoothed_image)
    plt.subplot(1,2,1)
    plt.imshow(numpyArray, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(  sitk.GetArrayFromImage(sobelImageSmooth), cmap='gray'  )
    plt.title('Edge Detection over Smoothed Image')
    plt.show()
