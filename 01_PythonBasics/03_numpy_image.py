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
