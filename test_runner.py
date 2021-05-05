import unittest
import tests.main_test as mt

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(mt.class_choise_test))
calcTestSuite.addTest(unittest.makeSuite(mt.class_menu_test))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)