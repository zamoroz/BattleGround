import Adventures,Fight

def menus(player,choise):
    choises = ["1","2","3"]
    if choise in choises:
        if choise == "1" :
            print(player)
            return player
        if choise == "2":
            result = Adventures.Adventures(player)
            return result
        if choise == "3" :
            return Fight.Fight(player)