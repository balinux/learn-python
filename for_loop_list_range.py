from curses import init_pair


nama = []
umur = []
banyak_data = int(input("masukkan jumlah data yang ingin di simpan: "))
for jumlah in range(0,banyak_data):
    print(f"masukkan data ke {jumlah+1}")
    input_nama = input("nama: ")
    input_umur = input("umur: ")

    nama.append(input_nama)
    umur.append(input_umur)

for data in range(0,len(nama)):
    dataNama = nama[data]
    dataUmur = umur[data]
    print("========")
    print("Daftar anggota")
    print("========")
    print(f"nama : {dataNama}")
    print(f"umur : {dataUmur}")