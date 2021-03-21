import sys
sys.path.append('../')
from typing import typing
from Enemy import Enemy
from random import choice

class dragon(Enemy):

    enemy_list = ["Красный дракон", "Синий дракон", "Зеленый дракон", "Черный дракон"]

    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = choice(self.enemy_list)
        self.type = "Дракон"
    
    def skill1(self):
        typing(self.name + " наносит удар лапой.")
        damage = 15 + self.strenght
        return damage
    
    def skill2(self):
        typing(self.name + " наносит удар хвостом.")
        damage = 20 + self.strenght
        return damage
        
    def skill3(self):
        typing(self.name + " извергает пламя.")
        damage = 25 + self.strenght
        return damage
