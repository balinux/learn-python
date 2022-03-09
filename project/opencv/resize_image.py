import cv2

img = cv2.imread('grey.jpg')
print("original Dimension: ", img.shape)

# menurunkan resize ke 60%
scale_percent = 30
width = int(img.shape[1] * scale_percent/100)
height = int(img.shape[0] * scale_percent/100)
dim = (width, height)

# resize image
resized = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

font = cv2.FONT_HERSHEY_SIMPLEX

# menambah text di image yang di resize
cv2.putText(resized, 'Balinux', (10, 200), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

cv2.putText(resized, 'Ganteng', (10, 500), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

print('Resized Dimensions : ',resized.shape)

cv2.imshow("resied", resized)

# menyyimpan gambar yang sudah di custom
key = cv2.waitKey(0) # menunggu untuk proses selanjutnya

if key == 27: # menunggu untuk tombol ESC
    cv2.destroyAllWindows()

elif key == ord('s'): # menunggu tombol 'S' di tekan dan melakukan proses simpan gambar
    cv2.imwrite('gambarbaru.jpg', resized)
    cv2.destroyAllWindows()


cv2.destroyAllWindows()

# referensi: https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/