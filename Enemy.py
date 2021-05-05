from random import randint, choice


import Item

class Enemy():
    
    def __init__(self, lvl):
        self.lvl = randint(lvl-2, lvl)
        if self.lvl < 0:
            self.lvl = 0
        self.strenght = randint(3,5) + self.lvl * 2
        self.dexterity = randint(3,5) + self.lvl * 2
        self.accuaracy = randint(3,5) + self.lvl * 2
        self.protection = randint(3, 5) + self.lvl * 2
        self.health = 20 + randint(1,10) + self.lvl*10
        self.treasure = []
    def add_health(self, i):
        self.health += i

    def short_info(self):
        return "Здоровье врага: " + str(self.health)

    def __str__(self):
        characteristics = { "Тип": self.type, "Уровень": self.lvl, "Здоровье": self.health, "Сила": self.strenght, "Ловкость": self.dexterity, "Точность": self.accuaracy, "Защита": self.protection}
        out = ''
        for i in characteristics:
            out += i + ': ' + str(characteristics.get(i)) + '\n'
        return out
    
    def randomSkill(self):
        skills = [1, 2, 3]
        skill = choice(skills)
        if skill == 1:
            return self.skill1()
        if skill == 2:
            return self.skill2()
        if skill == 3:
            return self.skill3()

    def getrandomtreause(self):
        quantOfTreaure = randint(1,3)
        for i in range(quantOfTreaure):
            item = Item.Item()
            self.treasure.append(item.as_dict())






