from randomEnemy import randomEnemy
from random import randint

class Fight():
    
    def __init__(self, player, enemy=None):
        self.player = player
        if enemy is None:
            self.enemy = randomEnemy(self.player.lvl)
        else:
            self.enemy = enemy
        
    def fight(self):
        player = self.player
        enemy = self.enemy

        def request():
            print(player.short_info())
            print("-"*30)
            print(enemy.short_info())
            print("-"*30)
            print("Как будем атаковать?")
            damage = self.player.skills()
            if damage is None:
                print("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                request()
            else:
                damage = self.hit(self.player, self.enemy, damage)
                self.enemy.add_health(-damage)
                print("Нанесено урона " + str(damage))
                print("-"*30)

        request()

        if enemy.health > 0:
            damage = self.hit(enemy, player, enemy.randomSkill())
            self.player.add_health(-damage)
            print("Нанесено урона " + str(damage))
            print("-"*30)
        if enemy.health <= 0:
            print("Вы убили " + enemy.name)
            print("-"*30)
            player.add_exp(30)
            return
        self.fight()

    def hit(self, attacker, defender, damage):
        if attacker.accuaracy < defender.dexterity and randint(1,2) < 2:
            print("Промах.")
            damage = 0
        elif attacker.strenght < defender.protection and randint(1,2) < 2:
            print("Заблокированано.")
            damage = 0
        return damage
        
    def direction(self):
        player = self.player
        enemy = self.enemy
        print("На тебя напал "+ enemy.name +".")
        print("Характеристики врага:")
        print(enemy)
        print("-"*30)
        def request():
            print("Что будешь делать?")
            print("1) Сражаться")
            print("2) Бежать")
            answer = input("> ")
            answers = ['1', '2']
            if answer in answers:
                if answer == "1":
                    print("Начинается бой с " + enemy.name)
                    self.fight()
                elif answer == "2":
                    if randint(1,10) < 8:
                        print("Убежать не удалось, придется сражаться...")
                        self.fight()
                    else:
                        print("Ты убежал от "+ enemy.name + ".")
                        print("-"*30)
                        player.add_exp(5)
            else:
                print("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                request()
        request()
