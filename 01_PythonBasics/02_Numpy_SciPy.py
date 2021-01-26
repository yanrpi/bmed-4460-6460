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
