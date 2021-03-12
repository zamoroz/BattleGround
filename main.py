import Player, Fight, Adventures
import sys, time

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    print("")

def characteristics(player):
    typing("Имя " + player.name)
    typing("Уровень " + str(player.lvl))
    typing("Сила " + str(player.strenght))
    typing("Ловкость " + str(player.dexterity))
    typing("Защита " + str(player.protection))
    typing("Здоровье " + str(player.health))
    typing("Уровень " + str(player.lvl))
    typing("Опыта до следующего уровня " + str(100 - player.exp))

def race_request():
    typing("Кто ты?")
    print("1) Человек")
    print("2) Гном")
    print("3) Эльф")
    race = input("> ")
    races = ["1", "2", "3"]
    if race in races:
        if race == "1":
            player.add_strenght(5)
        if race == "2":
            player.add_protection(5)
        if race == "3":
            player.add_dexterity(5)
    else: 
        typing("Ты что-то напутал, давай попробуем еще раз.")
        race_request()

def menu():
    typing("Что будем делать?")
    print("1) Узнать характеристики")
    print("2) Путешевствовать")
    print("3) Искать сражений")
    print("4) Посмотреть инвентарь")
    answer = input("> ")
    if answer == '1':
        characteristics(player)
    elif answer == '2':
        Adventures.Adventures(player)
    elif answer == '3':
        Fight.Fight(player)
    else: 
        typing("Ты что-то напутал, давай попробуем еще раз.")
    menu()

player = Player.Player()
typing("Приветствую путник!")
typing("Как тебя зовут?")
player.set_name(input("> "))
typing("Приятно познакомится, " + player.name + "!")   
race_request()
menu()