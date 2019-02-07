#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ******************************************
# yanrpi @2018
# ******************************************

import matplotlib.pyplot as plt

import numpy as np

from skimage import io
from skimage.feature import greycomatrix, greycoprops

import os
from os import path

import time

# %%

outPath     = r'./temp'
if not path.isdir(outPath):
    os.mkdir(outPath)

fName       = "GFP_06-DAPI.tif"
image       = io.imread(fName)

# Initialize feature images

contrastImage       = np.zeros(image.shape)
EnergyImage         = np.zeros(image.shape)
homogeneityImage    = np.zeros(image.shape)
correlationImage    = np.zeros(image.shape)
dissimilarityImage  = np.zeros(image.shape)

# %% Compute feature maps

def compute_glcm(patch):
    glcm = np.zeros((256, 256), dtype=np.int32)
    
    for i in range(patch.shape[0]):
        for j in range(patch.shape[1] - 3):
            glcm[patch[i,j], patch[i,j+3]] += 1
            
    return glcm[:,:,np.newaxis,np.newaxis]


# %%
    
st = time.time()
for i in range(image.shape[0]):
    
    if i % 5 == 0:
        ct = time.time()
        print('Precessing 5 rows at {} took {:.1f}s'.format(i, ct - st))
        st = ct
        
    # windows needs to fit completely in image
    if i < 3 or i > (image.shape[0] - 4):
        continue
    
    for j in range(image.shape[1] ):
        if j <3 or j > (image.shape[1] - 4):
            continue

        #Calculate GLCM on a 7x7 window
        glcm_window = image[i-3: i+4, j-3 : j+4]
        glcm = greycomatrix(glcm_window, 
                            [3], [0],  
                            symmetric = True, normed = True )
        #glcm = compute_glcm(glcm_window)

        # Calculate contrast and replace center pixel
        contrastImage[i,j]      = greycoprops(glcm, 'contrast')
        EnergyImage[i,j]        = greycoprops(glcm, 'energy')
        homogeneityImage[i,j]   = greycoprops(glcm, 'homogeneity')
        correlationImage[i,j]   =  greycoprops(glcm, 'correlation')
        dissimilarityImage[i,j]   =  greycoprops(glcm, 'dissimilarity')

# %%

def normalize_image(img):
    img = img / img.max() * 255
    return img.astype(np.ubyte)


contrastImage    = normalize_image(contrastImage)
EnergyImage      = normalize_image(EnergyImage)
homogeneityImage = normalize_image(homogeneityImage)
correlationImage = normalize_image(correlationImage)
dissimilarityImage = normalize_image(dissimilarityImage)


io.imsave(path.join(outPath, 'contrastImage.png'),
          contrastImage)
io.imsave(path.join(outPath, 'EnergyImage.png'),
          EnergyImage)
io.imsave(path.join(outPath, 'homogeneityImage.png'),
          homogeneityImage)
io.imsave(path.join(outPath, 'correlationImage.png'),
          correlationImage)
io.imsave(path.join(outPath, 'dissimilarityImage.png'),
          dissimilarityImage)

# %%
plt.figure()

plt.subplot(2,3,1)
plt.title('Input Image')
plt.imshow(image, cmap = 'gray')

plt.subplot(2,3,2)
plt.title('Contrast Image')
plt.imshow(contrastImage, cmap = 'gray')

plt.subplot(2,3,3)
plt.title('Energy Image')
plt.imshow(EnergyImage, cmap = 'gray')

plt.subplot(2,3,4)
plt.title('Homogeneity Image')
plt.imshow(homogeneityImage, cmap = 'gray')

plt.subplot(2,3,5)
plt.title('Correlation Image')
plt.imshow(correlationImage, cmap = 'gray')

plt.subplot(2,3,6)
plt.title('Dissimilarity Image')
plt.imshow(dissimilarityImage, cmap = 'gray')

plt.show()