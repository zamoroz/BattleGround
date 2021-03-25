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
    
    def unconscious_traveler(self):
        typing("Следуя зову приключений, ты натыкаешься на лежащего без сознания человека. Что будешь делать?")
        print("1) Осмотреть и попытаться помочь.")
        print("2) Поискать что-нибудь ценное у безсознательного путника.")
        print("3) Пройти мимо.")     
        solve = input("> ")
        solves['1','2','3']
        if solve in solves:
            if solve == '1':
                random_event = randint(1,2)
                if random_event == 1:
                    print("Вам удалось привести странника в чувства.")
                    print("Ох, что-то мне стало плохо по пути в город. Кажется я потерял сознания. Спасибо вам, если бы не вы, меня бы загрызли дикие звери!")
                    print("В качестве благодарности странник дарит вам подарок:")
                    #функция получения рандомной вещи
                else:
                    print("ЗАСАДА! На вас напали рабойники!")
                    #драка с разбойниками
            if solve == '2':
                random_event = randint(1,4)
                if random_event == 1:
                    print("Вам удалось найти ценную вещь и вы продолжили приключение.")
                    #функция получения рандомной вещи
                if random_event == 2:
                    print("Вы ничего ценного не нашли и продолжили приключени.")
                if random_event == 3:
                    print("О нет, вы разбудили путника!")
                    print("Что это вы делаете??? ГРАБИТЕЛЬ!!!")
                    #драка с путников
                else:
                    print("ЗАСАДА! На вас напали рабойники!")
                    #драка с разбойниками
            if solve == '3':
                return
        else:
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
            unconscious_traveler()
    unconscious_traveler()       
    
    
    def reward(self):
        pass