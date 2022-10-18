class Hero:
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
    
    # untuk menyerang hero lain maka gunakan class itu sendiri
    #contohya karna sven menginstance class Hero maka argument yang digunakna adalah Hero
    def doAttack(self, heroTarget):
        print(self.name + ' attack' , heroTarget.name)
        # bisa memanggil method lain
        heroTarget.gotAttack(self, self.attack)

    def gotAttack(self, attacker, damage):
        print(self.name, 'got attacket by', attacker.name)
        damage_receive = damage/self.armor
        print(f"total damage receive : {str(damage_receive)}")
        self.health -= damage_receive
        print(f"HP {self.name} tersisa {str(self.health)}")

sniper = Hero('sniper',100,10,4)
sven = Hero('sven', 160, 6, 10)

# argumen mengirin variabel bernama sven yang mengintance class Hero
sniper.doAttack(sven)
print("\n")
sven.doAttack(sniper)