# Author: Agnes Fusese
import unittest
from House_class import House

# __init__test

class TestStringMethods(unittest.TestCase):
    def test_init(self):
        House1 = House('Awoshie', 6, 1000000, True, 4)
        self.assertEqual(House1.PropertyLocation, 'Awoshie')

    #negative _init_test
    def test_Negative_init(self):
        House1 = House('Awoshie', 6, 1000000, True, 4)
        self.assertNotEqual(House1.PropertyLocation, 'Ghana')
 # testing rent status method
    def test_status(self):
        House1 = House('Awoshie', 6, 1000000, True, 4)
        self.assertEqual(House1.rented, True)

    #negative test for rent status
    def test_Negative_status(self):
        House1 = House('Awoshie', 6, 1000000, True, 4)
        self.assertNotEqual(House1.rented, False)

if __name__ == '__main__':
    unittest.main()