class Player:

    strenght: int #сила
    dexterity: int #ловкость
    protection: int #защита
    helth: int #здоровье
    name: str #имя
    exp: int
    lvl: int

    def __init__(self):
        self.strenght = 5
        self.dexterity = 5
        self.protection = 5
        self.health = 100
        self.name = ""
        self.exp = 0
        self.lvl = 1
        self.inventory = []
    
    def add_strenght(self, i):
        self.strenght += i
    
    def add_dexterity(self, i):
        self.dexterity += i
    
    def add_protection(self, i):
        self.protection += i

    def add_health(self, i):
        self.health += i
    
    def set_name(self, name):
        self.name = name
    
    def add_exp(self, i):
        self.exp += i
    
    def levelUp(self):
        self.lvl += 1
        self.exp = 0
        self.add_dexterity(self, 1)
        self.add_health(self, 10)
        self.add_protection(self, 1)
        self.add_strenght(self, 1)
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        pass