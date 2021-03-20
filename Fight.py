import Enemy
from random import randint
from typing import typing

class Fight:
    
    def __init__(self, player, enemy=None):
        self.player = player
        if enemy is None:
            self.enemy = Enemy.Enemy(self.player.lvl)
        else:
            self.enemy = enemy
        self.direction()
        
    def fight(self):
        player = self.player
        enemy = self.enemy

        damage = randint(1, player.strenght) - randint(1, enemy.protection)
        if damage < 1: damage = 1
        enemy.add_health(-damage)
        print("-"*30)
        typing("Ты нанес " + str(damage) + " урона врагу.")
        typing("Осталось " + str(enemy.health))

        damage = randint(1, enemy.strenght) - randint(1, player.protection)
        if damage < 1: damage = 1
        player.add_health(-damage)
        print("-"*30)
        typing(enemy.name + " нанес " + str(damage) + " урона тебе.")
        typing("Отсалось " + str(player.health))

        if player.health <= 0:
            print("-"*30)
            typing("Вы погибли.")
            input()

        if enemy.health <= 0:
            typing("Вы убили " + enemy.name)
            print("-"*30)
            player.add_exp(30)
            if player.exp >= 100:
                player.levelUp()
            return
        self.fight()

    def direction(self):
        player = self.player
        enemy = self.enemy
        typing("На тебя напал монстр "+ enemy.name +".")
        typing("Характеристики врага:")
        typing("Сила " + str(enemy.strenght))
        typing("Точность " + str(enemy.accuaracy))
        typing("Защита " + str(enemy.protection))
        typing("Здоровье " + str(enemy.health))
        print("-"*30)
        def solve_request():
            typing("Что будешь делать?")
            print("1) Сражаться")
            print("2) Бежать")
            solve = input("> ")
            solves = ['1', '2']
            if solve in solves:
                if solve == "1":
                    typing("Начинается бой с " + enemy.name)
                    self.fight()
                elif solve == "2":
                    if player.dexterity <= enemy.accuaracy:
                        typing("Убежать не удалось, придется сражаться...")
                        self.fight()
                    else:
                        typing("Ты убежал от монстра "+ enemy.name + ".")
                        print("-"*30)
                        player.add_exp(5)
                        if player.exp >= 100:
                            player.levelUp()
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                solve_request()
        solve_request()
