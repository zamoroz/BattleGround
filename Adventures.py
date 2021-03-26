from random import randint
from typing import typing
import Fight
from randomEnemy import enemyList
import sys
sys.path.append('enemies')
import human


class Adventures():

    def __init__(self, player):
        self.player = player
        place = randint(1, 5)
        if place == 1:
            self.lair()
        elif place == 2:
            self.__init__(self.player)
        elif place == 3:
            self.__init__(self.player)
        elif place == 4:
            self.__init__(self.player)
        elif place == 5:
            self.unconscious_traveler()

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
        solves = ['1','2','3']
        if solve in solves:
            if solve == '1':
                random_event = randint(1,2)
                if random_event == 1:
                    print("Вам удалось привести странника в чувства.")
                    typing("Ох, что-то мне стало плохо по пути в город. Кажется я потерял сознания. Спасибо вам, если бы не вы, меня бы загрызли дикие звери!")
                    print("В качестве благодарности странник дарит вам подарок:")
                    self.reward()
                else:
                    typing("ЗАСАДА! На вас напали рабойники!")
                    count = randint(2,6)
                    typing("Здесь " + str(count) + " разбойников.")
                    for i in range(count):
                        enemy = human.human(self.player.lvl)
                        enemy.name = "Разбойник"
                        Fight.Fight(self.player, enemy)
            if solve == '2':
                random_event = randint(1,4)
                if random_event == 1:
                    print("Вам удалось найти ценную вещь и вы продолжили приключение.")
                    self.reward()
                elif random_event == 2:
                    print("Вы ничего ценного не нашли и продолжили приключени.")
                elif random_event == 3:
                    print("О нет, вы разбудили путника!")
                    typing("Что это вы делаете??? ГРАБИТЕЛЬ!!!")
                    enemy = human.human(self.player.lvl)
                    enemy.name = "Путник"
                    Fight.Fight(self.player, enemy)
                else:
                    typing("ЗАСАДА! На вас напали рабойники!")
                    count = randint(2,6)
                    typing("Здесь " + str(count) + " разбойников.")
                    for i in range(count):
                        enemy = human.human(self.player.lvl)
                        enemy.name = "Разбойник"
                        Fight.Fight(self.player, enemy)
            if solve == '3':
                return
        else:
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
            self.unconscious_traveler()       
    
    def random_cave(self):
        typing("Вы продолжаете идти сквозь густой лес, пока внезапно не натыкаетесь на небольшую пещеру, манящую вас своей тайной... Что будете делать?")
        print("1) Осмотреть пещеру снаружи, не заходя в нее.")
        print("2) Войти внутрь пещеры.")
        print("3) Уйти от пещеры и продолжить путешевствие.")     
        solve = input("> ")
        solves = ['1','2','3']
        if solve in solves:
            if solve == '1':
                random_event = randint(1,5)
                if random_event == 1:
                    typing("Снаружи пещера выглядит безобидной, никакие постронноие звуки или запахи не привлекают вашего внимания.")
                    self.inspection_cave1()
                elif random_event ==2:
                    typing("В пещере издаются глухие но мощные звуки, похожие на дыхание какого-то огромного зверя. Похоже там спит дракон...")
                    print("1) Войти в пещеру и напасть на дракона.")
                    print("2) Продолжить путешевствие.")
                    solve = input("> ")
                    solves = ['1','2']
                    if solve in solves:
                        if solve == '1':
                            #атака на дракона
                        else:
                            self.__init__(self.player)
                elif random event == 3:
                    typing("Вы слышите как из пещеры раздаются чужие голоса. Возможно в ней кто-то разбил лагерь...")
                    print("1) Войти в пещеру.")
                    print("2) Продолжить путешевствие.")
                    solve = input("> ")
                    solves = ['1','2']
                    if solve in solves:
                        if solve == '1':
                            typing("Здравствуй путин! Мы простые путешевственники, как и ты. Присяд с нами у костра, да выпей с нами!")
                            #либо увеличение здоровья либо новый эликсир в подарок
                        else:
                            self.__init__(self.player)
                elif random_event == 4:
                    typing("Вы слышите сопение, рычание, вой, звуки чавканья. Скорее всего в пещере логого каких-то диких зверей... Что будете делать?")
                    print("1) Войти в пещеру и напасть на зверей.")
                    print("2) Продолжить путешевствие.")
                    solve = input("> ")
                    solves = ['1','2']
                    if solve in solves:
                        if solve == '1':
                            #атака на зверей
                        else:
                            self.__init__(self.player)
                else:
                    typing("ЗСАДА! Как только вы подходите к пещере, чтобы осмотреть ее, на вас нападают разбойники!")
                    count = randint(2,6)
                    typing("Здесь " + str(count) + " разбойников.")
                    for i in range(count):
                        enemy = human.human(self.player.lvl)
                        enemy.name = "Разбойник"
                        Fight.Fight(self.player, enemy)
            if solve == '2':
                random_event = randint(1,4)
                if random_event == 1:
                    print("Вам удалось найти ценную вещь и вы продолжили приключение.")
                    self.reward()
                elif random_event == 2:
                    print("Вы ничего ценного не нашли и продолжили приключени.")
                elif random_event == 3:
                    print("Внутри пещеры оказался зверь, который тут же бросился на вас!")
                    #атака зверя
                else:
                    typing("Внутри пещеры оказался лагерь разбойников. Увидев вас, они тут же ринулись в бой!")
                    count = randint(2,6)
                    typing("Здесь " + str(count) + " разбойников.")
                    for i in range(count):
                        enemy = human.human(self.player.lvl)
                        enemy.name = "Разбойник"
                        Fight.Fight(self.player, enemy)
            if solve == '3':
                return
        else:
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
            self.random_cave()   
    
    
    def inspection_cave():
        random_event = randint(1,3)
        if random_event == 1:
            typing("Пещера оказалсь пуста. Вы продолжили свое путешевствие...")
            self.__init__(self.player)
        elif random_event == 2:
            typing("Ого! В пещере вы нашли сокровище!")
            self.reward()
        else 
            typing("ЗСАДА! Как только вы подходите к пещере, чтобы осмотреть ее, на вас нападают разбойники!")
            count = randint(2,6)
            typing("Здесь " + str(count) + " разбойников.")
            for i in range(count):
                enemy = human.human(self.player.lvl)
                enemy.name = "Разбойник"
                Fight.Fight(self.player, enemy)
                
                
    def inspection_cave2():
        
    
    
    def reward(self):
        pass
