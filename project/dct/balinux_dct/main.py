# Import functions and libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy
import cv2

from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc # pip install Pillow
import matplotlib.pylab as pylab

# %matplotlib inline
pylab.rcParams['figure.figsize'] = (20.0, 7.0)


# im = misc.imread("einstein.tif").astype(float)
# im = misc.imread("house.tif").astype(float)
im = cv2.imread('lena.png',0).astype(float)
# im = misc.imread("lena.png").astype(float)
print(im)
# im = misc.imread("barbara.png").astype(float)

# 
# Define 2D DCT and IDCT
# 
def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'), axis=1 , norm='ortho')


# 
# Extract 8x8 block and look at its DCT coefficients¶
# 
imsize = im.shape
dct = np.zeros(imsize)
pos = 128

# Extract a block from image
plt.subplot(131),plt.imshow(im[pos:pos+8,pos:pos+8],cmap='gray')
plt.title('An 8x8 Image block'), plt.xticks([]), plt.yticks([])

# Display the dct of that block
plt.subplot(132),plt.imshow(dct[pos:pos+8,pos:pos+8],cmap='gray',vmax= np.max(dct)*0.01,vmin = 0, extent=[0,pi,pi,0])
plt.title('An 8x8 DCT block'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(im, cmap = 'gray')
plt.title('Input back'), plt.xticks([]), plt.yticks([])

# # Extract a block from image
# plt.figure()
# plt.imshow(im[pos:pos+8,pos:pos+8],cmap='gray')
# plt.title( "An 8x8 Image block")

# # Display the dct of that block
# plt.figure()
# plt.imshow(dct[pos:pos+8,pos:pos+8],cmap='gray',vmax= np.max(dct)*0.01,vmin = 0, extent=[0,pi,pi,0])
# plt.title( "An 8x8 DCT block")


# # display noraml iage gryscale
# f = plt.figure()
# plt.imshow(im,cmap='gray')
# plt.subplot(121),plt.imshow(im, cmap = 'gray')

plt.show()