import sys
sys.path.append('../')
from typing import typing
from Player import Player

class warrior(Player):

    def __init__(self):
        super().__init__()
        self.max_rage = 100
        self.rage = 0

    def add_rage(self, i):
        self.rage += i
        if self.rage > self.max_rage:
            self.rage = self.max_rage
    
    def skill_dependence(self):
        return "1) Обычная атака. \n2) Сильная атака. \n3)Очень сильная атака"
        
    def skill1(self):
        typing("Вы бьете врага.")
        damage = 5 + self.lvl
        self.add_rage(10)
        return damage
    
    #удар тратит ярость и накапливает
    def skill2(self):
        if self.rage >= 15:
            typing("Вы наносите сильную атаку.")
            damage = 10 + self.lvl
            self.add_rage(-10)
            return damage
        else:
            typing("Не хватает ярости.")

    def skill3(self):
        if self.rage >= 25:
            typing("Вы наносите очень сильную атаку.")
            damage = 20 + self.lvl
            self.add_rage(-20)
            return damage
        else:
            typing("Не хватает ярости.")

    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Ярость": self.rage, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuracy, "Интелект":self.intelligence, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out