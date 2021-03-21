import Fight, Adventures
import sys
from typing import typing
sys.path.append('class')
import mage, warrior, assasin

class main():

    def __init__(self):
        typing("Приветствую путник!")
        typing("Как тебя зовут?")
        self.player_name = (input("> "))
        typing("Приятно познакомится, " + self.player_name + "!")   
        self.requests()
        self.menu()

    def requests(self):
        typing("Кто ты?")
        print("1) Маг")
        print("2) Воин")
        print("3) Убийца")
        race = input("> ")
        races = ["1", "2", "3"]
        if race in races:
            if race == "1":
                self.player = mage.mage()
                self.player.set_name(self.player_name)
            if race == "2":
                self.player = warrior.warrior()
                self.player.set_name(self.player_name)
            if race == "3":
                self.player = assasin.assasin()
                self.player.set_name(self.player_name)
        else: 
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
            self.requests()

    def menu(self):
        typing("Что будем делать?")
        print("1) Узнать характеристики")
        print("2) Путешевствовать")
        print("3) Искать сражений")
        print("4) Посмотреть инвентарь")
        answer = input("> ")
        answers = ['1', '2', '3']
        if answer in answers:
            if answer == '1':
                print(self.player)
            elif answer == '2':
                Adventures.Adventures(self.player)
            elif answer == '3':
                Fight.Fight(self.player)
        else: 
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
        self.menu()

if __name__ == "__main__":
    main()