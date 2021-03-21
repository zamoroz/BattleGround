import sys
sys.path.append('../')
from typing import typing
from Player import Player

class assasin(Player):

    def __init__(self):
        super().__init__()
        self.max_energy = 100
        self.energy = self.max_energy
    
    def add_energy(self, i):
        self.energy += i
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def skill_dependence(self):
        return "1) Обычная атака. \n2) Сильная атака. \n3)Очень сильная атака"

    def skill1(self):
        typing("Вы бьете врага.")
        damage = 5 + self.lvl
        self.add_energy(10)
        return damage
    
    def skill2(self):
        if self.energy >= 15:
            typing("Вы наносите сильную атаку.")
            damage = 10 + self.lvl
            self.add_energy(-15)
            return damage
        else:
            typing("Не хватает ярости.")

    def skill3(self):
        if self.energy >= 25:
            typing("Вы наносите очень сильную атаку.")
            damage = 20 + self.lvl
            self.add_energy(-25)
            return damage
        else:
            typing("Не хватает ярости.")

    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Ярость": self.energy, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuracy, "Интелект":self.intelligence, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out