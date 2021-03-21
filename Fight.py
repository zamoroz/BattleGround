from randomEnemy import randomEnemy, randomSkill
from random import randint
from typing import typing

class Fight:
    
    def __init__(self, player, enemy=None):
        self.player = player
        if enemy is None:
            self.enemy = randomEnemy(self.player.lvl)
        else:
            self.enemy = enemy
        self.direction()
        
    def fight(self):
        player = self.player
        enemy = self.enemy

        def request():
            typing(player.short_info())
            print("-"*30)
            typing(enemy.short_info())
            print("-"*30)
            typing("Как будем атаковать?")
            print(player.skill_description())
            answer = input(">")
            answers = ['1', '2', '3']
            if answer in answers:
                if answer == '1':
                    self.hit(player, enemy, player.skill1())
                if answer == '2':
                    self.hit(player, enemy, player.skill2())
                if answer == '3':
                    self.hit(player, enemy, player.skill3())
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                request()
        request()

        self.hit(enemy, player, randomSkill(enemy))

        if enemy.health <= 0:
            typing("Вы убили " + enemy.name)
            print("-"*30)
            player.add_exp(30)
            return
        self.fight()

    def hit(self, attacker, defender, damage):
        if attacker.accuaracy < defender.dexterity and randint(1,10) < 5:
            typing("Промах.")
            damage = 0
        elif attacker.strenght < defender.protection and randint(1,10) < 5:
            typing("Заблокированано.")
            damage = 0
        defender.add_health(-damage)
        print("Нанесено урона " + str(damage))
        print("-"*30)

    def direction(self):
        player = self.player
        enemy = self.enemy
        typing("На тебя напал монстр "+ enemy.name +".")
        typing("Характеристики врага:")
        print(enemy)
        print("-"*30)
        def request():
            typing("Что будешь делать?")
            print("1) Сражаться")
            print("2) Бежать")
            answer = input("> ")
            answers = ['1', '2']
            if answer in answers:
                if answer == "1":
                    typing("Начинается бой с " + enemy.name)
                    self.fight()
                elif answer == "2":
                    if randint(1,10) < 8:
                        typing("Убежать не удалось, придется сражаться...")
                        self.fight()
                    else:
                        typing("Ты убежал от монстра "+ enemy.name + ".")
                        print("-"*30)
                        player.add_exp(5)
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                request()
        request()
