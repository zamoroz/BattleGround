from random import randint, choice

class Enemy():
    
    def __init__(self, lvl):
        self.lvl = randint(lvl-3, lvl)
        if self.lvl < 0:
            self.lvl = 0
        self.strenght = randint(1,5) + self.lvl
        self.dexterity = randint(1,5) + self.lvl
        self.accuaracy = randint(1,5) + self.lvl
        self.protection = randint(1, 5) + self.lvl
        self.health = 20 + randint(1,10) + self.lvl*10
        
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