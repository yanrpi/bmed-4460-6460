#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ******************************************
# yanrpi @2018
# ******************************************

import time
import numpy as np
import matplotlib.pyplot as plt

from skimage import io

from sklearn.cluster import KMeans

from os import path

# %%

outPath = r'./temp'
fName = "GFP_06-DAPI.tif"

X = io.imread(fName)
nx, ny = X.shape

XN = X.astype(np.float)

# 

contrastImage       = io.imread(path.join(outPath, 'contrastImage.png'))
EnergyImage         = io.imread(path.join(outPath, 'EnergyImage.png'))
homogeneityImage    = io.imread(path.join(outPath, 'homogeneityImage.png'))
dissimilarityImage  = io.imread(path.join(outPath, 'dissimilarityImage.png'))

# %%

nx,ny = X.shape

nFeatures = 5

FEATS = np.zeros((nx,ny,nFeatures))
FEATS[:,:,0] = X
FEATS[:,:,1] = contrastImage
FEATS[:,:,2] = EnergyImage
FEATS[:,:,3] = homogeneityImage
FEATS[:,:,4] = dissimilarityImage

#F = X.reshape((nx*ny, 1))
F = FEATS.reshape((nx*ny, nFeatures))

# %%

num_clusters = 2
k_means = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)

print('Performing k-means clustering...')

t0 = time.time()
k_means.fit(F)
et = time.time() - t0

print('k-means completed in {:.1f}s'.format(et))

k_means_labels = k_means.labels_

k_means_img = k_means_labels.reshape((nx,ny))

def normalize_image(img):
    img = img / img.max() * 255
    return img.astype(np.ubyte)

k_means_img = normalize_image(k_means_img)

# %%

plt.imshow(k_means_img)
plt.show()

fNameOut = path.join(outPath, 'Kmeans_Texture_{}.png'.format(num_clusters))  
print("Clustering result saved into: {}".format(fNameOut))
io.imsave(fNameOut, k_means_img)

print("DONE")
