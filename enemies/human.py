from typing import typing
from Enemy import Enemy
from random import choice

class human(Enemy):

    enemy_list = ["Разбойник", "Грабитель"]

    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = choice(self.enemy_list)
        self.type = "Человек"
        self.treasure = self.getrandomtreause()
    
    def skill1(self):
        typing(self.name + " наносит удар.")
        damage = 10 + self.strenght
        return damage
    
    def skill2(self):
        typing(self.name + " наносит удар.")
        damage = 15 + self.strenght
        return damage
        
    def skill3(self):
        typing(self.name + " наносит удар.")
        damage = 20 + self.strenght
        return damage
