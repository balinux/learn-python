from modul_calculator import hitung


print("masukkan tinggi badan(*cm): ")
tinggi_badan = int(input())

print("masukkan berat badan(*kg): ")
berat_badan = int(input())

jumlah = hitung(tinggi_badan,berat_badan)
print(f"data: Body Mass Index (BMI):  {jumlah[0]}, {jumlah[1]}")