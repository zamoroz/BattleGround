from random import randint,choice

class Enemy:

    strenght: int #сила
    accuaracy: int #точность
    protection: int #защита
    health: int #здоровье
    name: str #имя
    enemy_names_list = ["Гоблин", "Хобгоблин", "Слизь", "Волк", "Крыса", "Зомби"]
    
    def __init__(self, lvl):
        self.strenght = randint(1,5) + lvl
        self.accuaracy = randint(1,7) + lvl
        self.protection = randint(1, 5) + lvl
        self.health = 20 + randint(1,10) + lvl*10
        self.name = choice(self.enemy_names_list)
    
    def add_health(self, i):
        self.health += i
    
    def set_name(self, name):
        self.name = name
