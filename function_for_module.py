def say_hello(name):
    return f"hello {name}"

def total(*list_angka):
    hasil = 0
    for data in list_angka:
        hasil = hasil + data
    return hasil

