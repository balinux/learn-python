class Hero:
    jumlah_hero = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    # method void, method yang digunakan tanpa mereturn apapun
    def greeting(self):
        print(f"i'm : {self.name}")
    
    def attackLifeSteal(self, stealPerHit):
        self.health += stealPerHit * self.health

    def gethealth(self):
        return self.health

sniper = Hero('sniper', 100, 10, 5)
sven = Hero('sven', 300, 4, 15)

# sniper part
# print(sniper.__dict__)
sniper.greeting()
sniper.attackLifeSteal(0.03)
print(f"sniper health {sniper.gethealth()}")
# print(sniper.__dict__)