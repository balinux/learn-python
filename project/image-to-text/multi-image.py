from PIL import Image
from pytesseract import pytesseract
from pathlib import Path
import os

path_dir = str(Path(__file__).absolute().parent)

imageData = path_dir + "/images" 

for root, dir, files in os.walk(imageData):
    for file in files:
        # print(file)
        text = pytesseract.image_to_string(imageData + "/" + file)
        print(text)
# print(text)