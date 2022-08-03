from PIL import Image
from pytesseract import pytesseract
from pathlib import Path

path_dir = str(Path(__file__).absolute().parent)

imageData = path_dir + "/images/example.png" 

text = pytesseract.image_to_string(imageData)
print(text)