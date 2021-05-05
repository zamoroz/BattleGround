from typing import typing
import Fight, Adventures
from class_choice import class_choice

class main():

    def __init__(self):
        typing("Вы проcнулись в своей каюте от крика чаек и шума волн, бьющихся о корму корабля. Открыв глаза вы увидели лучи света, проникающие сквозь редкие деревянные щели.")
        typing("Выйдя из каюты, вы ощутили как дневной свет щипет вам глаза. Когда ваши глаза привыкли к яркости окружающего мира, вы оглядели окружающее вас пространство.")
        typing("Ваш корабль пришвартовался к берегу, а команда матросов неумолимо трудилась под командованием капитана. Как только вы ощутили твердую почву под ногами, сойдя с корабля, вы увидели бегущево к вам низкорослого, полноватого человека.")
        typing("Приветствую вас господин и добро пожаловать в Адвентовиль! Меня зовут Сайрокс, я служащий учетной службы. Чтобы пустить вас в город, мне нобходимо уточнить у вас некоторые детали.")
        typing("Лоцман достал перо и пергамент из путевой сумки и приготовился записывать:")
        typing("Ваше имя, сэр?")
        player_name = (input("> "))
        typing("Лоцман внес " + player_name + " в пергамен.")   
        self.requests()
        self.player.set_name(player_name)
        self.menu()

    def requests(self):
        typing("Скажите, какими способносятми вы обладаете?")
        print("1) Маг")
        print("2) Воин")
        print("3) Убийца")
        self.player = class_choice(input("> "))       
        if self.player is None:
            typing("Погодите... вы меня разыгрываете? Давайте попробуем еще раз:")
            print("-"*30)

    def menu(self):
        typing("Что будем делать?")
        print("1) Узнать характеристики")
        print("2) Путешевствовать")
        print("3) Искать сражений")
        print("4) Посмотреть инвентарь")
        print("5) Надеть предметы ")
        answer = input("> ")
        answers = ['1', '2', '3','4','5']
        if answer in answers:
            if answer == '1':
                print(self.player)
            elif answer == '2':
                Adventures.Adventures(self.player)
            elif answer == '3':
                Fight.Fight(self.player)
            elif answer == '4':
                print(self.player.inventory)
            elif answer == '5':
                if len(self.player.inventory) == 0 :
                    print('Твой инвентарь пуст, нечего надеть')
                else:
                    print(self.player.inventory)
                    print('Чего надевать будем?')
                    selectedItem = int(input())
                    self.player.equipment.equip(self.player.inventory[selectedItem])




        else: 
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
        self.menu()

if __name__ == "__main__":
    main()