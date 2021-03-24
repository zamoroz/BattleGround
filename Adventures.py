from random import randint
from typing import typing
import Fight
from randomEnemy import enemyList

class Adventures():

    adventures_list = ["Пещера", "Город", "Логово монстров", "Лагерь разбойников"]

    def __init__(self, player):
        self.player = player
        place = "Логово монстров"
        if place == "Пещера":
            self.cave()
        elif place == "Город":
            self.__init__(self.player)
        elif place == "Логово монстров":
            self.lair()
        elif place == "Лагерь разбойников":
            self.camp()

    def lair(self):
        count = randint(1,10)
        lst = enemyList(self.player.lvl, count)
        typing("Во время своих путешествий ты набрел на логово монстра типа " + lst[0].type + ".")
        typing("Здесь обитает " + str(count) + " монстров.")
        def solve_request():
            typing("Что будем делать?")
            print("1) Напасть")
            print("2) Искать приключения дальше")
            print("3) Выбрать другое действие")
            solve = input("> ")
            solves = ['1', '2', '3']
            if solve in solves:
                if solve == '1':
                    for i in lst:
                        Fight.Fight(self.player, i)
                    self.reward()
                    return
                if solve == '2':
                    self.__init__(self.player)
                if solve == '3':
                    return
            else:
                typing("Ты что-то напутал, давай попробуем еще раз.")
                print("-"*30)
                solve_request()
        solve_request()
    
    def reward(self):
        pass