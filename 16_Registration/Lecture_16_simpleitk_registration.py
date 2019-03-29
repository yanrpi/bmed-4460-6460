# Demo image registration using SimpleITK

from matplotlib import pyplot as plt
import numpy as np
import SimpleITK as sitk

# %%

fn_img0 = 'img0.png'
img0 = sitk.ReadImage(fn_img0)
print(img0.GetOrigin())
print(img0.GetSpacing())
print(img0.GetDirection())

# %% Get numpy array from image

img0_array = sitk.GetArrayFromImage(img0)

#plt.imshow(img0_array, cmap='gray')
#plt.show()

# %% Read Image for Registration

fixed_image =  sitk.ReadImage('img0.png', sitk.sitkFloat32)
moving_image = sitk.ReadImage('img1.png', sitk.sitkFloat32)

# %% Use the CenteredTransformInitializer to align the centers of 
#   the two volumes and set the center of rotation to the center 
#   of the fixed image.

initial_transform = sitk.CenteredTransformInitializer(
    fixed_image, 
    moving_image, 
    sitk.Euler2DTransform(), 
    sitk.CenteredTransformInitializerFilter.GEOMETRY)

#initial_transform = sitk.Transform(2, sitk.sitkIdentity)

moving_resampled = sitk.Resample(moving_image, 
                                 fixed_image,
                                 initial_transform,
                                 sitk.sitkLinear,
                                 0.0,
                                 moving_image.GetPixelID()) # output pixel type

# %% Start Image Registration

registration_method = sitk.ImageRegistrationMethod()

# Similarity metric settings.
#registration_method.SetMetricAsCorrelation()
registration_method.SetMetricAsMeanSquares()

registration_method.SetInterpolator(sitk.sitkLinear)

# Optimizer settings.
registration_method.SetOptimizerAsGradientDescent(
    learningRate=0.1, 
    numberOfIterations=100, 
    convergenceMinimumValue=1e-6, 
    convergenceWindowSize=10)

# The number of iterations involved in computations are defined by 
# the convergence window size

# Estimating scales of transform parameters a step sizes, from the 
# maximum voxel shift in physical space caused by a parameter change. 
registration_method.SetOptimizerScalesFromPhysicalShift()

# Initialize registration
registration_method.SetInitialTransform(initial_transform, inPlace=False)

# %%

# Callback invoked when the StartEvent happens, sets up our new data.
def clear_values():
    global metric_values
    
    metric_values = []

# Callback invoked when the IterationEvent happens, update our data 
# and display new figure.    
def save_values(registration_method):
    global metric_values
    value = registration_method.GetMetricValue()
    metric_values.append(value)
    #print('It {}: metric value {:.4f}'.format(
    #    len(metric_values), value))
    
    
# Connect all of the observers so that we can perform plotting 
# during registration.
registration_method.AddCommand(sitk.sitkStartEvent, 
                               clear_values)
registration_method.AddCommand(sitk.sitkIterationEvent, 
                               lambda: save_values(registration_method))

final_transform = registration_method.Execute(fixed_image, 
                                              moving_image)

print('Final metric value: {0}'.format(
    registration_method.GetMetricValue()))
print('Optimizer\'s stopping condition, {0}'.format(
    registration_method.GetOptimizerStopConditionDescription()))

moving_resampled = sitk.Resample(moving_image,
                                 fixed_image,
                                 final_transform,
                                 sitk.sitkLinear,
                                 0.0,
                                 moving_image.GetPixelID())

moving_resampled = sitk.Cast(moving_resampled, sitk.sitkUInt8)
sitk.WriteImage(moving_resampled, 'moving_resampled.png')
sitk.WriteTransform(final_transform, 'final_transform.txt')
