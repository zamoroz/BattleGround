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

    def levelUp(self):
        super().levelUp()
        self.add_dexterity(1)
        self.add_accuaracy(1)

    def skill_description(self):
        return "1) Быстрая атака. \n2) Атака со спины. \n3)Концентрация на уклонении. \n4)Бросить бомбу"

    def skill1(self):
        typing("Вы быстро атакуете.")
        damage = 10 + self.dexterity
        self.add_energy(10)
        return damage
    
    def skill2(self):
        if self.energy >= 20:
            typing("Вы бьете врага в спину.")
            damage = 20 + self.dexterity
            self.add_energy(-20)
            return damage
        else:
            typing("Не хватает выносливости.")

    def skill3(self):
        if self.energy >= 25:
            typing("Вы сконцентрировались на уклонении.")
            shield = 10 + self.dexterity
            self.add_energy(-25)
            return shield
        else:
            typing("Не хватает выносливости.")

    def skill4(self):
        if self.energy >= 30:
            typing("Вы бросаете бомбу во врага.")
            damage = 30 + self.accuaracy
            self.add_energy(-30)
            return danage
        else:
            typing("Не хватает выносливости.")

    def short_info(self):
        return "Здоровье: " + str(self.health) + "\nВыносливость: " + str(self.energy)

    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Щит": self.shield, "Выносливость": self.energy, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuaracy, "Интелект":self.intelligence, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out