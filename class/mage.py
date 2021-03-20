import sys, time
sys.path.append('../')
from random import choice
from Player import Player

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

class mage(Player):
    
    mana: int

    def __init__(self):
        super().__init__()
        self.mana = 100
    
    def add_mana(self, i):
        self.mana += i
    
    def levelUp(self):
        super().levelUp()
        self.add_mana(30)
    
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