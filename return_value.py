# method prosedur adalah method yang menjalan/mengeksekusi kode program saja

# method function adalah method yang mengembalikan sebuah nilai


def jumlah(*listangka):
  total=0;
  for angka in listangka:
    total = total + angka
  return total

total = jumlah(33,44,55)

print(total)


# menggunakan tuple untuk return banyak data

def jumlah2(*listangka):
  total=0
  for angka in listangka:
    total = total + angka
  return (listangka, total)

total = jumlah2(33,44,55)

print(f"Total {listangka} : {total}")