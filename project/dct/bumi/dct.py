import cv2
import numpy as np
from matplotlib import pyplot as plt

#citra awal
cf = cv2.imread('lena.png',0)
rows, cols = cf.shape

#transformasi fourier
f = np.fft.fft2(cf)
fshift = np.fft.fftshift(f)
mag2 = 20*np.log(np.abs(fshift))

#pengolahan pada frekuensi domain, implementasi High Pass Filter
crow,ccol = int(rows/2) , int(cols/2)
fshift[crow-50:crow+50, ccol-50:ccol+50] = 0
mag3 = 20*np.log(np.abs(fshift))

#transformasi balik
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)


fig,axs = plt.subplots(1, 4, figsize=(15, 15))
axs[0].imshow(cf, cmap='gray', vmin=0, vmax=255)
axs[0].set_title("citra awal")
axs[1].imshow(mag2, cmap='gray', vmin=0, vmax=255)
axs[1].set_title("Mag. Spectrum")
axs[3].imshow(img_back, cmap='gray')
axs[3].set_title("Hasil HP filter")
axs[2].imshow(mag3, cmap='gray', vmin=0, vmax=255)
axs[2].set_title("HP filter")
plt.show()