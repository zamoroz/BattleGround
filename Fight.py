from randomEnemy import randomEnemy
from typing import typing
from random import randint

class Fight():
    
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
            damage = self.player.skills()
            if damage is None:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                request()
            else:
                self.hit(self.player, self.enemy, damage)

        request()

        if enemy.health > 0:
            self.hit(enemy, player, enemy.randomSkill())
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
        typing("На тебя напал "+ enemy.name +".")
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
                        typing("Ты убежал от "+ enemy.name + ".")
                        print("-"*30)
                        player.add_exp(5)
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                request()
        request()
