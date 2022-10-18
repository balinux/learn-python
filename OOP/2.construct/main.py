
class Hero:
    # secara default attribute class tidak ada
    # untuk membuat atribute variable pada class maka gunakan variable stataic dengan cara di bawah ini
    jumlan = 0

    def __init__(self, name, inputHp):
        # dibawah ini merupakan instance variable yang mana akan dimiliki oleh kelas yang menginstance itu sendiri
        self.name = name
        self.hp = inputHp
        Hero.jumlan += 1 # bagian ini berfungsi menambah jumlah saat class di instance
        print(f"membuat hero dengan nama {name}")

hero1 = Hero("sniper", 100)
print(Hero.jumlan) # variabel static bisa di panggil
hero2 = Hero("sven", 110)
print(Hero.jumlan) # variabel static bisa di panggil
hero3 = Hero("axe", 120)
print(Hero.jumlan) # variabel static bisa di panggil

# cara mengecek attribute class
# print(Hero.__dict__)
# setelah di instance maka akan terlihat jumlah sudah ada di attribute class Hero