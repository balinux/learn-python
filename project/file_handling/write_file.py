# membuat python untuk menulis string data kedalam file
import os
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.txt'

# if file_location.is_file():
#     # print("file exist")
#     print("input data: ")
#     string_data = input()
#     file = open(file_location, 'w')
#     file.write(string_data)
#     file.close
# else:
#     print("file not exist")


# # menggunakan mode penambahan atau append mode
# if file_location.is_file():
#     print("input data: ")
#     string_data = input()
#     file = open(file_location, 'a')
#     file.write(string_data)
#     file.close
# else:
#     print("file not exist")


# # mengguakan WITH fuction
# if file_location.is_file():
#     with open(file_location) as file:
#         data = file.read()
#         print(data)
# else:
#     print("file not exist")


# menggunakan split untuk memisah kalimat menjadi array string
# input : Feby dan Khalid pergi kondangan
if file_location.is_file():
    with open(file_location,'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split()
            print(word) # output : ['Feby', 'dan', 'Khalid', 'pergi', 'kondangan']
else:
    print("file not exist")