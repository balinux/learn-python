class Hero:
    pass
hero1 = Hero()
hero2 = Hero()
hero3 = Hero()

hero1.name = 'sniper'
hero1.hp = 100

hero2.name = 'sven'
hero2.hp = 130

print(hero2.__dict__)
print(hero2.name)