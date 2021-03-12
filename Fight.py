import Enemy
from random import randint
import sys, time

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

class Fight:
    
    def __init__(self, player, enemy=None):
        self.player = player
        if enemy is None:
            self.enemy = Enemy.Enemy()
        else:
            self.enemy = enemy
        self.direction()
        
    def fight(self):
        player = self.player
        enemy = self.enemy
        print(player.name)
        print("/HP/St/Pr")
        print(str(player.health) + "/" + str(player.strenght) + "/" + str(player.protection))
        print("-"*15)
        print(enemy.name)
        print("/HP/St/Pr")
        print(str(enemy.health) + "/" + str(enemy.strenght) + "/" + str(enemy.protection))
        print("-"*15)

        damage = randint(1, player.strenght) - randint(1, enemy.protection)
        if damage < 1: damage = 1
        typing("Ты нанес " + str(damage) + " урона врагу.")
        enemy.add_health(-damage)

        damage = randint(1, enemy.strenght) - randint(1, player.protection)
        if damage < 1: damage = 1
        typing(enemy.name + " нанес " + str(damage) + " урона тебе.")
        player.add_health(-damage)

        if player.health <= 0:
            typing("Вы погибли.")
            input()

        if enemy.health <= 0:
            typing("Вы убили " + enemy.name)
            player.add_exp(15)
            return

        if player.exp >= 100:
            player.levelUp()
        self.fight()

    def direction(self):
        player = self.player
        enemy = self.enemy
        typing("Ты искал битвы и нашел себе врага.")
        typing("Характеристики врага:")
        typing("Имя " + enemy.name)
        typing("Сила " + str(enemy.strenght))
        typing("Точность " + str(enemy.accuaracy))
        typing("Защита " + str(enemy.protection))
        typing("Что будешь делать?")
        def solve_request():
            typing("1)Сражаться")
            typing("2)бежать")
            solve = input("> ")
            if solve == "1":
                typing("Начинается бой с " + enemy.name)
                self.fight()
            elif solve == "2":
                if player.dexterity < enemy.accuaracy:
                    typing("Убежать не удалось, придется сражаться...")
                    self.fight()
                else:
                    typing("Ты убежал от этого врага, но кто знает, что ждеть тебя в следующую секунду.")
                    player.add_exp(5)
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                solve_request()
        solve_request()
