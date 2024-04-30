#Doreen Lawratu Baidoo
import unittest
from Land_Class import Land

# __init__test

class TestStringMethods(unittest.TestCase):
    def test_init(self):
        Land1 = Land('Kigali', 67, 345654, False, 540)
        self.assertEqual(Land1.PropertyLocation, 'Kigali')

    #negaitve __init_ test
    def test_Negative_init(self):
        Land1 = Land('Kigali', 67, 345654, False, 540)
        self.assertNotEqual(Land1.PropertyLocation, 'Nyarutarama')

    # testing rent status method
    def test_status(self):
        Land1 = Land('Kigali', 67, 345654, False, 540)
        self.assertEqual(Land1.rented, False)

    #negative test for rent status
    def test_Negative_status(self):
        Land1 = Land('Kigali', 67, 345654, False, 540)
        self.assertNotEqual(Land1.PropertyLocation, True)

    #testing Land_info in land class
    def test_land_info(self):
        Land1 = Land('Kigali', 67, 345654, False, 540)
        self.assertEqual(Land1.Land_info,("Location of land: " + "Kigali" + " Price of Land: " +
                         str(345654) + " Land Size: " + str(540)))



if __name__ == '__main__':
    unittest.main()