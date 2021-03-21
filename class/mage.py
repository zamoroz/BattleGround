import sys
sys.path.append('../')
from random import choice
from Player import Player
from typing import typing

class mage(Player):

    def __init__(self):
        super().__init__()
        self.max_mana = 100
        self.mana = self.max_mana
    
    def add_mana(self, i):
        self.mana += i
        if self.mana > self.max_mana:
            self.mana = self.max_mana
    
    def levelUp(self):
        super().levelUp()
        self.add_max_mana(10)
        self.mana = self.max_mana
    
    def skill1(self):
        typing("Вы бьете врага посохом.")
        damage = 5 + self.lvl
        print("Нанесено урона: " + str(damage))
    
    def skill2(self):
        if self.mana >= 10:
            elements  = ["огненный", "водяной", "каменный", "електрический"]
            typing("Вы бросаете во врага малый " + elements.choise() + " шар.")
            damage = 10 + self.lvl
            print("Нанесено урона: " + str(damage))
            self.add_mana(-10)
        else:
            typing("Не хватает маны.")

    def skill3(self):
        if self.mana >= 20:
            elements  = ["огненный", "водяной", "каменный", "електрический"]
            typing("Вы бросаете во врага " + elements.choise() + " шар.")
            damage = 20 + self.lvl
            print("Нанесено урона: " + str(damage))
            self.add_mana(-20)
        else:
            typing("Не хватает маны.")
        
    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Мана": self.mana, "Сила": self.strenght, "Ловкость": self.dexterity, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ' : ' + str(characteristics.get(i)) + '\n'
        return out