# referensi : https://www.geeksforgeeks.org/python-os-rename-method/?ref=lbp

import os
from pathlib import Path

file_name = "tes.txt"
path_source = str(Path(__file__).absolute().parent) + "/from/" + file_name
path_target = str(Path(__file__).absolute().parent) + "/to/" + file_name

os.rename(path_source, path_target)


