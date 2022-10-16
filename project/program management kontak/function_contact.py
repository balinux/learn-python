def display_contact(contact_list):
    for contact in contact_list:
        print("-------------------")
        print(f"nama : {contact['name']} ")
        print(f"email : {contact['email']} ")
        print(f"phone : {contact['phone']} ")

def add_contact():
    name = input("name: ")
    email = input("email: ")
    phone = input("phone: ")
    contact = {
        "name" : name,
        "email" : email,
        "phone" : phone,
    }
    return contact

def remove_contact(contact_list):
    name = input("masukkan nama contact yang ingin di hapus: ")

    index = -1
    
    for i in range(0, len(contact_list)):
        if name == contact_list[i]["name"]:
            index = i
            break
    if index == -1:
        print("data tidak ditemukan")
    else:
        del contact_list[index]
        print("berhasil menghapus data")
    # return contact_list

def find_contact(contact_list):
    name_search = input("masukkan nama yang di cari")

    for contact in contact_list:
        name = contact["name"]
        # find akan mengembalikan index string, jika tidak ditemukan maka return -1
        if name.find(name_search) != -1:
            print("-------------------")
            print(f"nama : {contact['name']} ")
            print(f"email : {contact['email']} ")
            print(f"phone : {contact['phone']} ")
        else:
            print("kontak yang di cari tidak ditemukan")
