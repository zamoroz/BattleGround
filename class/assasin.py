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
        self.add_strenght(1)

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
        return "1) Обычная атака накапливает энергию, низкий урон. \n2) Сильная атака тратит 15 энергии, средний урон. \n3) Очень сильная атака тратит 25 энергии, большой урон "

    def skill1(self):
        typing("Вы бьете врага.")
        damage = 10 + self.strenght
        self.add_energy(10)
        return damage
    
    def skill2(self):
        if self.energy >= 15:
            typing("Вы наносите сильную атаку.")
            damage = 15 + self.strenght
            self.add_energy(-15)
            return damage
        else:
            typing("Не хватает энергии.")

    def skill3(self):
        if self.energy >= 25:
            typing("Вы наносите очень сильную атаку.")
            damage = 20 + self.strenght
            self.add_energy(-25)
            return damage
        else:
            typing("Не хватает энергии.")

    def short_info(self):
        return "Здоровье: " + str(self.health) + "\nЭнергия: " + str(self.energy)

    def __str__(self):
        characteristics = { "Имя": self.name, "Уровень": self.lvl, "Здоровье": self.health, "Енергия": self.energy, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuaracy, "Интелект":self.intelligence, "Защита": self.protection, "Опыта до уровня": 100-self.exp}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out