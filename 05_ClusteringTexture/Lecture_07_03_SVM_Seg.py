#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ******************************************
# yanrpi @2018
# ******************************************

import numpy as np
import matplotlib.pyplot as plt

from skimage import io

from sklearn import svm
from sklearn import preprocessing

from os import path
import time

# %%

outPath = r'./temp'
fName = "GFP_06-DAPI.tif"

fGradient = path.join(outPath, 'GFP_06-DAPI_dx1dy.tif')
fPositive = path.join(outPath, 'Annotations_CellPositive_Mask.tif')
fNegative = path.join(outPath, 'Annotations_CellNegative_Mask.tif')
IGradient = io.imread(fGradient)
IPositive = io.imread(fPositive)
INegative = io.imread(fNegative)

idxPositive = IPositive > 0
idxNegative = INegative > 0

X = io.imread(fName)
nx,ny = X.shape

XN = X.copy().astype(np.float)

# %%

nFeatures = 2
FEATS = np.zeros((nx,ny,nFeatures))
FEATS[:,:,0] = X
FEATS[:,:,1] = IGradient
#F = X.reshape((nx*ny, 1))

#Mean Values: 
print(FEATS[idxPositive,0].mean())
print(FEATS[idxPositive,1].mean())

print(FEATS[idxNegative,0].mean())
print(FEATS[idxNegative,1].mean())

min_max_scaler = preprocessing.MinMaxScaler()
for k in range(nFeatures): 
    FEATS[:,:,k] = min_max_scaler.fit_transform(FEATS[:,:,k])

FeatP = FEATS[idxPositive,:]
FeatN = FEATS[idxNegative,:]

nTraningPositive = FeatP.shape[0]
nTraningNegative = FeatN.shape[0]

idxPositiveSample = np.random.choice( range(nTraningPositive), size = 300)
idxNegativeSample = np.random.choice( range(nTraningNegative), size = 300)

FeatP = FeatP[idxPositiveSample,:]
FeatN = FeatN[idxNegativeSample,:]

nTraningPositive = FeatP.shape[0]
nTraningNegative = FeatN.shape[0]

# put together training set
XTraining = np.concatenate((FeatP, FeatN), axis=0)
penalty = 1000

myKernel = 'rbf'

clf = svm.SVC(kernel=myKernel, C=penalty, verbose=True)

YLabels = [1] * nTraningPositive + [0] * nTraningNegative

t0 = time.time()
clf.fit(XTraining, YLabels)
et = time.time() - t0

print('SVM trained in {:.1f}s'.format(et))

# %% Testing

XNPred = XN.reshape((XN.size , 1))

F = FEATS.reshape((nx*ny, nFeatures))
Z = clf.predict( F )
print("DONE")

# %%

# Put the result into a color plot
Z = Z.reshape(X.shape)

plt.imshow(Z)
plt.show()

fNameOut = path.join(outPath, 'SVM_{}.png'.format(myKernel))

Z = Z * 255
Z = Z.astype(np.ubyte)
io.imsave(fNameOut, Z)

print('Image saved into {}'.format(fNameOut))

