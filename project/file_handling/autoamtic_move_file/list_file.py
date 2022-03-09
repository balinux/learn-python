from fileinput import filename
import os
from pathlib import Path

path_dir = str(Path(__file__).absolute().parent)

print(path_dir)
list_of_file = []

# fungsi yang digunakan untuk memindahkan file
# gunakan path lengkap
# extention digunakan untuk menentukan penempatan file sesuai folder
def movingFile(ext, file_path, file):
    if ext == '.jpg':
        path_target = str(Path(__file__).absolute().parent) + "/image/" + file
        os.rename(file_path, path_target)
    elif ext =='.txt':
        print("ini text")
        path_target = str(Path(__file__).absolute().parent) + "/text/" + file
        os.rename(file_path, path_target)

for root, dirs, files in os.walk(path_dir):
    for file in files:
        filename, file_ext = os.path.splitext(file)
        #  print(file_ext)
        # print(os.path.join(root, file))
        movingFile(file_ext, os.path.join(root, file), file)


