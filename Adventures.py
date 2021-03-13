from random import choice, randint
import sys, time
import Fight
import Enemy

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

class Adventures:

    adventures_list = ["Пещера", "Город", "Логово монстров", "Лагерь разбойников"]

    def __init__(self, player):
        self.player = player
        place = "Пещера"
        if place == "Пещера":
            self.cave()
        elif place == "Город":
            self.__init__(self.player)
        elif place == "Логово монстров":
            self.lair()
        elif place == "Лагерь разбойников":
            self.camp()

    def cave(self, enemy = None):
        if enemy is None:
            enemy = Enemy.Enemy(self.player.lvl)
        count = randint(1,10)
        typing("Во время своих путешествий вы набрели на пещеру монстра: " + enemy.name)
        typing("Здесь обитает " + str(count) + " " + enemy.name)
        typing("Что быдем делать?")
        print("1) Нападасть")
        print("2) Искать приключения дальше")
        print("3) Выбрать друго действие")
        answer = input("> ")
        if answer == '1':
            for i in range(count):
                new_enemy = Enemy.Enemy(self.player.lvl)
                new_enemy.set_name(enemy.name)
                Fight.Fight(self.player, new_enemy)
            self.reward()
        if answer == '2':
            self.__init__(self.player)
        if answer == '3':
            return
        else:
            typing("Ты что-то напутал, давай попробуем еще раз.")
            self.cave(enemy)
    
    def reward(self):
        pass