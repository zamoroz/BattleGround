from random import randint,choice

class Enemy:

    strenght: int #сила
    accuaracy: int #точность
    protection: int #защита
    health: int #здоровье
    name: str #имя
    enemy_names_list = ["Гоблин", "Хобгоблин", "Слизь", "Волк", "Крыса", "Зомби", "Разбойник"]
    
    def __init__(self):
        self.strenght = randint(1,10)
        self.accuaracy = randint(1,15)
        self.protection = randint(1,10)
        self.health = 20 + randint(1,15)
        self.name = choice(self.enemy_names_list)
    
    def add_health(self, i):
        self.health += i
    
    def set_name(self, name):
        self.name = name
