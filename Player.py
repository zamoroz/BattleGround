from typing import typing

class Player:

    def __init__(self):
        self.strenght = 5
        self.dexterity = 5
        self.protection = 5
        self.intelligence = 5
        self.accuracy = 5
        self.max_health = 100
        self.health = self.max_health
        self.name = ""
        self.exp = 0
        self.lvl = 0

    def add_strenght(self, i):
        self.strenght += i
    
    def add_dexterity(self, i):
        self.dexterity += i
    
    def add_protection(self, i):
        self.protection += i

    def add_intelligence(self, i):
        self.intelligence += i
    
    def add_accuracy(self, i):
        self.accuracy += i

    def add_health(self, i):
        self.health += i
        if self.health > self.max_health:
            self.health = self.max_health
        elif self.health <= 0:
            typing("Вы погибли!")
            input()
    
    def set_name(self, name):
        self.name = name
    
    def add_exp(self, i):
        self.exp += i
        if self.exp >= 100:
            self.exp = 0
            self.levelUp()
    
    def add_max_health(self, i):
        self.max_health += i
    
    def levelUp(self):
        typing("Поздравляю! вы повысили уровень, все характеристики выросли.")
        self.lvl += 1
        self.exp = 0
        self.add_max_health(20)
        self.health = self.max_health
        self.add_dexterity(1 + int(0.5 * self.lvl))
        self.add_protection(1 + int(0.5 * self.lvl))
        self.add_strenght(1 + int(0.5 * self.lvl))
        self.add_intelligence(1 + int(0.5 * self.lvl))
        self.add_accuracy(1 + int(0.5 * self.lvl))
    