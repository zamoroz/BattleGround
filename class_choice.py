import classes.mage as mage
import classes.warrior as warrior
import classes.assasin as assasin

def class_choice(choice):
    choices = ["1", "2", "3"]
    if choice in choices:
        if choice == "1":
            return mage.mage()
        if choice == "2":
            return warrior.warrior()
        if choice == "3":
            return assasin.assasin()