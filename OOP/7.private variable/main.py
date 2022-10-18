# private variable berbeda dengan variable pada class, dan instance class yang bisa di akses oleh object lain
# jika contoh pada hero, private biasa digunakan untuk mengamankan data seperti XP musuh.

class Hero:
    # class variable bersifat public 
    jumlahHero = 0
    def __init__(self, name, health) :
        # variable instance bersifat public
        self.name = name
        self.health = health

        # variable instance bersifat private, tinggal menambahkan 2 underscore
        self.__private = "private"

        # variable instance protected
        self._protectted = "protected"

mirana = Hero("mirana",100)
# variabel bersifat public pada instance bisa dilihat disini
print(mirana.__dict__)
print(mirana.__private)
print(mirana.health)