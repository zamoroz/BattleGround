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
        self.lvl = 0
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
        self.add_dexterity(1 + int(0.5 * self.lvl))
        self.add_health(30)
        self.add_protection(1 + int(0.5 * self.lvl))
        self.add_strenght(1 + int(0.5 * self.lvl))
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        pass