# documentation
# https://www.geeksforgeeks.org/file-handling-python/
# https://stackoverflow.com/questions/12201928/open-gives-filenotfounderror-ioerror-errno-2-no-such-file-or-directory

import os
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.txt'
# print(file_location)

if file_location.is_file():
    # print("file exist")
    file = open(file_location,'r')
    for each in file:
        print(each)
else:
    print("file not exist")
