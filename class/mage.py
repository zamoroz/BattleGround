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
    
    def skills(self):
        print("1) Обычная атака. \n2) Сильная атака. \n3) Очень сильная атака. \n4) Подробнее")
        answer = input(">")
        answers = ['1', '2', '3', '4']
        if answer in answers:
            if answer == '1':
                return self.skill1()
            if answer == '2':
                return self.skill2()
            if answer == '3':
                return self.skill3()
            if answer == '4':
                print(self.skill_description())
                input("Назад")
                return self.skills()

    def skill_description(self):
        return "1) Обычная атака не тратит маны, низкий урон. \n2) Сильная атака тратит 10 маны, средний урон. \n3) Очень сильная атака тратит 20 маны, большой урон "

    def skill1(self):
        typing("Вы бьете врага.")
        damage = 5 + self.strenght
        return damage
    
    def skill2(self):
        if self.mana >= 10:
            typing("Вы бросаете во врага малый " + choice(self.elements) + " шар.")
            damage = 15 + self.intelligence
            self.add_mana(-10)
            return damage
        else:
            typing("Не хватает маны.")

    def skill3(self):
        if self.mana >= 20:
            typing("Вы бросаете во врага " + choice(self.elements) + " шар.")
            damage = 25 + self.intelligence
            self.add_mana(-20)
            return damage
        else:
            typing("Не хватает маны.")

    def short_info(self):
        return "Здоровье: " + str(self.health) + "\nМана: " + str(self.mana)
        
    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Мана": self.mana, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuaracy, "Интелект":self.intelligence, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out