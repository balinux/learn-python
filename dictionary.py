# untuk array selain list, set, dan tuple adalagi namanya dictionary

customer = {"name": "rio", "age": 20}

name = customer["name"]
age = customer["age"]

# mengumbah data di dictionary
customer["name"] = "khalid"

# menambah data di dictionary 
customer["ayah"] = "rio"

# menghapus data di dictionary
del customer["age"]

# cara 1 untuk mengambil value dari list
# for key in customer:
#     value = customer[key]
#     print(f"{key} : {value}")

# cara 2 untuk mengambil value dari list
for key, value in customer.items():
    print(f"{key} : {value}")
