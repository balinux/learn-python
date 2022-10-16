import function_contact

contact_data =[]
contact_data.append({
    "name" : "balinux",
    "email" : "balinux@yhotie.com",
    "phone" : "123123123",
})

# Menu Program
while True:
    print('#Menu')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. hapus Kontak')
    print('4. Cari Kontak')
    print('0. keluar program')

    menu = input("Pilih Menu :")

    if menu == "0":
        break
    elif menu == "1":
        function_contact.display_contact(contact_data)
    elif menu == "2":
        new_contact = function_contact.add_contact()
        contact_data.append(new_contact)
    elif menu =="3":
        function_contact.remove_contact(contact_data)
    elif menu == "4":
        function_contact.find_contact(contact_data)
    else:
        print("menu tidak tersedia")
        
print('program selesai berjalan, sampai jumpa')
