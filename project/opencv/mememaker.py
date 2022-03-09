import cv2

# menampung image
img = cv2.imread("grey.jpg");

# (0,0): titik awal garis
# (511, 511): titik ahir garis
# (233, 236, 18): warna garins
# 5: ketebalan garis
cv2.line(img,(0,0),(511,511),(223,236,18),5)

# menampilkan gambar
cv2.imshow('line on image', img)

# membuat persegi
cv2.rectangle(img, (384, 0), (510, 128), (80,18,236), 2)

# membuat persegi full
cv2.rectangle(img, (684, 300), (110, 128), (80,18,236), -1)

cv2.imshow('rectangle on image', img) 

# tombol yang digunakan untuk melanjutkan aktivitas
cv2.waitKey(0)

# mengeluarkan open cv
cv2.destroyAllWindows()