'''
Created for course 4460/6460 - Biological Image Analysis

@author: Pingkun Yan
'''

import numpy as np

"Numpy Examples"


'''Declares List  '''
myList = [1, 2, 3, 4]

'''Declares array '''
X = np.array(myList)
print(X)              #[1 2 3 4]

'''Get the size '''
print(X.shape)        #(4,)
print(X.dtype)        #int32 or int64

'''unsigned 8 Bit  '''
print(np.uint8)
X = np.array(myList, np.uint8)

print(X)

X[0] = 255          # ???
print(X[0])         #

X[0] = 256          # ???
print(X[0])         #

X[0] = 259          # ???
print(X[0])         #

# %%

'''linspace '''
X = np.linspace(0, 20, 5)
print(X)            # [  0.   5.  10.  15.  20.]

X = np.linspace(0, 20, 100)
print(X)            
print(X.shape)      #100

'''Vector Operations'''
X = np.linspace(0, 20, 5)
X = X + 10

print(X)
print(X.min())
print(X.max())
print(X.mean())
print(X % 2)

# %% quiz

'''Indexing '''
print(X)        #[ 10.  15.  20.  25.  30.]
idx = X == 20


print(idx)      #[False False  True False False]
print(X[idx])    #???
print(X[~idx])   #???

idy = X > 20
print(X)         #[ 10.  15.  20.  25.  30.]
print(idy)       #???
print(X[idy])    #???
print(X[~idy])   #???

'''Example of OR operation '''

idz = idx | idy
# Write an equivalent expression: idz = X ?? 20
print(idz)       #???
print(X[idz])    #???

# %%

'''Import imageio and pyplot '''
import imageio
import matplotlib.pyplot as plt

fName = "GFP_06-DAPI.tif"

I = imageio.imread(fName)

'''Print basic image statis '''
print(I.shape)       #(634, 800)
print(I.dtype)       #uint8
print(I.min())       #6
print(I.max())       #137
print(I.mean())      #20.53

'''Plot Image '''
plt.imshow(I)   #load
plt.show()      # show the window

# %%

'''Get histogram and plot '''
hist, bins = np.histogram(I, bins=50)

print(hist)  
'''[ 90730 225236  36759  14362   7505   3608   4404   3938   4707   5389
   5980   8206  10552   6778  10048   5246   8637   8048   4271   6531
   4584   3320   3497   2363   3034   3103   1630   2336   1430   1813
   1476    935   1084   1013    559    578    350    321    326    153
    271    207    162    358    340    426    332    152    101     11] 
'''
print(bins)
'''
[   6.      8.62   11.24   13.86   16.48   19.1    21.72   24.34   26.96
   29.58   32.2    34.82   37.44   40.06   42.68   45.3    47.92   50.54
   53.16   55.78   58.4    61.02   63.64   66.26   68.88   71.5    74.12
   76.74   79.36   81.98   84.6    87.22   89.84   92.46   95.08   97.7
  100.32  102.94  105.56  108.18  110.8   113.42  116.04  118.66  121.28
  123.9   126.52  129.14  131.76  134.38  137.  ]
'''
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2

plt.bar(center, hist, align='center', width=width)
plt.show()

# %%

'''Map the intensity in the log2 '''
ILog = np.log2(I, dtype=np.float32)
plt.imshow(ILog)   #load
plt.show()      # show the window
hist, bins = np.histogram(ILog, bins=50)

width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()

# %%

'''Global Threshold'''
T = 20
idx = I > 20
plt.imshow(idx)
plt.show()

# %%

'''Report Area and Intensity in Segmentation Mask'''
nPixels    = len(I[idx])
PercentArea =  100.0 * float(nPixels) / float(I.size) 
print("Number of Pixels in Mask: ", nPixels)         #131296
print("Percent Area: ",             PercentArea)     #25.88

print("Mean Intensity in Mask: ", I[idx].mean())     #50.782
print("Max Intensity in Mask: ",  I[idx].max())      #137
print("Min Intensity in Mask: ",  I[idx].min())      #21

# %%

from scipy.ndimage import measurements
ILabel, nFeatures = measurements.label(idx)
print("Number of elements: ", nFeatures)
plt.imshow(ILabel)
plt.show()

# %%

'''Report Intensity Per Object'''
for k in range(nFeatures):
    idxCell = ILabel == k
    print("Cell: ", k, " Mean: ", I[idxCell].mean())
    
