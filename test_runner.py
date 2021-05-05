import unittest
import tests.main_test as mt
import tests.fight_test as ft

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(mt.class_choise_test))
#calcTestSuite.addTest(unittest.makeSuite(mt.class_menu_test))
calcTestSuite.addTest(unittest.makeSuite(ft.fight_test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)