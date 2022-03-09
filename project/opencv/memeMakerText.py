import cv2

# menampung image
img = cv2.imread("grey.jpg");

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img, 'Balinux', (10, 200), font, 4, (255, 255, 255), 5, cv2.LINE_AA)

cv2.putText(img, 'Ganteng', (10, 500), font, 4, (255, 255, 255), 5, cv2.LINE_AA)

cv2.imshow('meme', img) 

    # image: The variable holding our image
    # 'Balinux': The text you want to be printed on the screen
    # (10, 200): The bottom left corner of where the message starts from
    # font: The font type of the text you want
    # 4 : This is font scale
    # (255, 255, 255): The colour of the text
    # 2: The thickness of the text
    # cv2.LINE_AA: The line type used

# It shows the image on the screen. The first argument is for the image title
# and the second is for the image variable. 

# tombol yang digunakan untuk melanjutkan aktivitas
cv2.waitKey(0)

# mengeluarkan open cv
cv2.destroyAllWindows()