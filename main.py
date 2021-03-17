import Player, Fight, Adventures
import sys, time

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

class main():

    def __init__(self):
        self.player = Player.Player()
        typing("Приветствую путник!")
        typing("Как тебя зовут?")
        self.player.name = (input("> "))
        typing("Приятно познакомится, " + self.player.name + "!")   
        self.requests()
        self.menu()

    def characteristics(self):
        player = self.player
        typing("Имя " + player.name)
        typing("Уровень " + str(player.lvl))
        typing("Сила " + str(player.strenght))
        typing("Ловкость " + str(player.dexterity))
        typing("Защита " + str(player.protection))
        typing("Здоровье " + str(player.health))
        typing("Опыта до уровня " + str(100 - player.exp))
        print("-"*30)

    def requests(self):
        typing("Кто ты?")
        print("1) Человек")
        print("2) Гном")
        print("3) Эльф")
        race = input("> ")
        races = ["1", "2", "3"]
        if race in races:
            if race == "1":
                self.player.add_health(20)
            if race == "2":
                self.player.add_protection(2)
            if race == "3":
                self.player.add_dexterity(2)
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
        answers = ['1', '2', '3', '4']
        if answer in answers:
            if answer == '1':
                self.characteristics()
            elif answer == '2':
                Adventures.Adventures(self.player)
            elif answer == '3':
                Fight.Fight(self.player)
            elif answer == '4':
               print(self.player.inventory)
        else: 
            typing("Ты что-то напутал, давай попробуем еще раз.")
            print("-"*30)
        self.menu()

if __name__ == "__main__":
    main()