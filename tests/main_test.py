from Adventures import Adventures
import unittest
import menus
import class_choice
import Player

class class_choise_test(unittest.TestCase):
    def test_assasin(self):
        character = class_choice.class_choice("3")
        self.assertEqual(character.type, 'Убийца')
    
    def test_mage(self):
        character = class_choice.class_choice("1")
        self.assertEqual(character.type, 'Маг')

    def test_war(self):
        character = class_choice.class_choice("2")
        self.assertEqual(character.type, 'Воин')


class class_menu_test(unittest.TestCase):
    def test_first_way(self):
        player = Player.Player
        self.assertEqual(menus.menus(player,"1"), player)

    '''def test_second_way(self):
        player = Player.Player
        self.assertIn(menus.menus(player,"2").place, range(1,5))'''

    def test_assert_true(self):
        player = Player.Player
        #self.assertTrue(type(menus.menus(player,"2")) is Adventures)
        self.assertIsInstance(menus.menus(player,"2"), Adventures)