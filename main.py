# # print string
# print("hello world")

# #print number
# print(15)


# #Math
# #tambah
# print(2+2)

# #kurang
# print(5-3)

# #bagi
# print(12/3)

# #kali
# print(5*10)

# #sisa bagi
# print(10 %3)


# # Variabe
# variable1 = "hello"

# print(variable1)



# # Belajar String
# var1 = "rio"
# var2 = "juniyantara"

# nama_lengkap =var1+" "+var2

# print(nama_lengkap)



# # String format
# var1 = "Muhammad"
# var2 = "Khalid"

# nama_lengkap = f"halo {var1} {var2}"
# print(nama_lengkap)



# #input data
# print("masukkan nama anda:")

# nama = input()

# print(f"selamat datang {nama}")



# # Input number
# # by default input dari python adalah string
# print("masukkan angka pertama yang ingin di jumlahkan")

# angka1 = int(input())

# print("masukkan angka kedua yang ingin di jumlahkan")

# angka2 = int(input())

# jumlah = angka1 + angka2

# print(f"jumlah {angka1} + {angka2} : {jumlah}")




# Operator logika

# print(True and True)
# print(True and False)
# print(False and False)



#operator perbandingan comparison
# == 	Equal 	 	
# != 	Not equal  	
# > 	Greater than 	
# < 	Less than 	 	
# >= 	Greater than or equal to 	 	
# <= 	Less than or equal to 	

# print(1>4)
# print(1<4)
# print(1<=1)



# # if statment

# usia = 26
# dewasa = 25

# if usia < dewasa:
#   print(f"anda masih belum dewasa usia anda: {usia} tahun")

# if usia > dewasa:
#   print(f"anda sudah dewasa usia anda: {usia} tahun")

# if usia == dewasa:
#   print(f"anda baru meranjak dewasa usia anda: {usia} tahun")



# #if else statement
# #kapan melakukan if else : yaitu saat opsi cukup 2 saja misalkan boolean

# status = False

# if status == True:
#   print("selamat anda menang")
# else:
#   print("coba lebih keras lagi")



# # else if statement menggunakan elif

# menu_pilihan =int(input("silahkan pilih menu [1-3]:"))

# if menu_pilihan == 1:
#   print("anda memesan ayam")

# elif menu_pilihan == 2:
#   print("anda memilih menu lele")

# elif menu_pilihan == 3:
#   print("anda memilih menu sate")

# else:
#   print("silahkan pilih menu yang sesuai yang disediakan")



# # type data List

# nama = ["rio","linda","rian"]

# # menambah data ke list
# nama.append("daos")

# # mencetak salah satu data di list
# nama_urut1 = nama[0]
# print(nama_urut1)

# # mencetak panjang list
# print( f"panjang list nama adalag: {len(nama)}")

# # mengurangi data di list
# nama.remove("rio")
# print(nama)

# # update list

# nama[0] = "khalid"
# print(nama)



# #for loop
# nama = ["rio","linda","rian"]

# nama.append("daos")

# for data in nama:
#   print(f"nama dengan nomor urut {nama.index(data) + 1 } : {data}")



# #tipe data range

# # data = range(1,11)

# # for number in data:
# #   print(number)

# # atau bisa juga menggunakan range langsung compile
# for number in range(1,11):
#   print(number)



# # contoh aplikasi menggunakan for-loop, list, dan range

# nama = []
# umur = []

# banyak_data = int(input("masukkan berapa banyak data yang akan anda simpan: "))

# for jumlah in range(0,banyak_data):
#   print(f"data ke {jumlah+1}: ")
#   input_nama = input("nama: ")
#   input_umur = input("umur: ")

#   nama.append(input_nama)
#   umur.append(input_umur)

# for data in range(0,len(nama)):
#   dataNama = nama[data]
#   dataUmur = umur[data]
#   print(f"##################")
#   print(f" nama : {dataNama} ") 
#   print(f" umur : {dataUmur} ") 




# # perulangan menggunakan while

# data = ""

# while data !="x":
#   print("masukkan perulangan")
#   data= input("data: ")




# belajar continue
# continue berfungsi untuk menskip proses di bawahnya
# hasil print adalah ganjil karna genap di filter

# for i in range(1,100):
#   if i % 2 == 0:
#     continue
#   print(i) 





# belajar break
# digunakan untuk menghentikan perulangan atau menghentikan proses
# looping akan berhenti pada nomor 49

# contoh 1
# for i in range(1,100):
#   if i % 50 == 0:
#     break
#   print(i)

# contoh 2
# berhenti jika input adalah = x
# while True:
#   data = input("data: ")
#   if data == "x":
#     break
#   print(data)




# belajar tuple
# tuple merupakan data immutable/ tidak bisa di ubah

pelanggan = ('aaa','bbb','ccc')

print(pelanggan)
print(pelanggan[2])