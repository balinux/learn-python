from PIL import Image
from pytesseract import pytesseract
from pathlib import Path
import cv2

path_dir = str(Path(__file__).absolute().parent)

imageData = path_dir + "/images/example.png" 

# grayscale
greyscale = cv2.cvtColor(imageData,cv2.COLOR_BGR2GRAY)

cv2.imshow('img', greyscale)
# text = pytesseract.image_to_string(imageData)
# print(text)