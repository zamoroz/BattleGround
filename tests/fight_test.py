from Fight import Fight
from classes.mage import mage
from randomEnemy import randomEnemy
import unittest

class fight_test(unittest.TestCase):
    def test_skill1(self):
        player = mage()
        fight = Fight(player)
        enemy = randomEnemy(player.lvl)
        self.assertIs(type(fight.hit(player, enemy, player.skill1())), int)

    def test_skill2(self):
        player = mage()
        fight = Fight(player)
        enemy = randomEnemy(player.lvl)
        self.assertIs(type(fight.hit(player, enemy, player.skill2())), int)
    
    def test_skill3(self):
        player = mage()
        fight = Fight(player)
        enemy = randomEnemy(player.lvl)
        self.assertIs(type(fight.hit(player, enemy, player.skill3())), int)