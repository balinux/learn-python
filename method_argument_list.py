def jumlah(var1, var2):
  total = var1 + var2
  print(f"total: {[var1, var2]} = {total}")

jumlah(10,10)



# default param

def jumlah2(var1, var2, var3=0):
  total = var1 + var2 +var3
  print(f"total: {[var1, var2, var3]} = {total}")

jumlah2(10,10)


# menggunakan list argument
# jika ingin menambahkan argumen selain list, maka taruh argumen tersebut di depan

def jumlah3(*listangka):
  total=0;
  for angka in listangka:
    total = total + angka
    print(f"Total = {listangka} = {total}")

jumlah3(33,44,55)