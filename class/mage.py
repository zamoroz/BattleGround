import sys
sys.path.append('../')
from random import choice
from Player import Player
from typing import typing

class mage(Player):

    elements  = ["огненный", "водяной", "каменный", "електрический"]

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
        self.add_intelligence(2)
    
    def skill_description(self):
        return "1) Атака посохом. \n2) Атака элементом. \n3) Магический щит \n4) Призыв элемнталя"

    def skill1(self):
        typing("Вы бьете врага посохом.")
        damage = 5 + self.strenght
        return damage
    

    def skill2(self):
        if self.mana >= 20:
            typing("Вы бросаете во врага " + choice(self.elements) + " шар.")
            damage = 25 + self.intelligence
            self.add_mana(-20)
            return damage
        else:
            typing("Не хватает маны.")

    def skill3(self):
        if self.mana >= 20:
            typing("Вы создаете " + choice(self.elements) + " щит.")
            shield = 15 + self.intelligence
            self.add_mana(-20)
            return shield
        else:
            typing("Не хватает маны.")
            
    def skill4(self):
        if self.mana >= 30:
            typing("Вы призываете " + choice(self.elements) + " элементаля.")
            self.add_mana(-30)
            return elemental
        else:
            typing("Не хватает маны.")            

    def short_info(self):
        return "Здоровье: " + str(self.health) + "\nМана: " + str(self.mana)
        
    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Щит": self.shield, "Мана": self.mana, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuaracy, "Интелект":self.intelligence, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out