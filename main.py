from typing import typing
import Fight, Adventures
import sys
sys.path.append('class')
import mage, warrior, assasin

class main():

    def __init__(self):
        typing("Вы проcнулись в своей каюте от крика чаек и шума волн, бьющихся о корму корабля. \nОткрыв глаза вы увидели лучи света, проникающие сквозь редкие деревянные щели.")
        typing("Выйдя из каюты, вы ощутили как дневной свет щипет вам глаза. \nКак только ваши глаза привыкли к яркости окружающего мира, вы оглядели окружающее вас пространство.")
        typing("Ваш корабль пришвартовался к берегу, а команда матросов неумолимо трудилась под командованием капитана.\nКак только вы ощутили твердую почву под ногами, сойдя с корабля, \nвы увидели бегущево к вам низкорослого, полноватого человека.")
        typing("Приветствую вас господин и добро пожаловать в Адвентовиль!\nМеня зовут Сайрокс, я служащий учетной службы. \nЧтобы пустить вас в город, мне нобходимо уточнить у вас некоторые детали.")
        typing("Лоцман достал перо и пергамент из путевой сумки и приготовился записывать:")
        typing("Ваше имя, сэр?")
        self.player_name = (input("> "))
        typing("Лоцман внес " + self.player_name + " в пергамен.")   
        self.requests()
        self.menu()

    def requests(self):
        typing("Скажите, какими способносятми вы обладаете?")
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
            typing("Погодите... вы меня разыгрываете? Давайте попробуем еще раз:")
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