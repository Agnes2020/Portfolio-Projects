#Author Doreen Lawuratu Baidoo
import unittest
from Property_class import Property


# __init__test

class TestStringMethods(unittest.TestCase):
    def test_init(self):
        Property1 = Property('Kigali', 67, 345654, False)
        self.assertEqual(Property1.PropertyLocation, 'Kigali')

    # negative __init__ test
    def test_negative_init(self):
        Property1 = Property('Kigali', 67, 345654, False)
        self.assertNotEqual(Property1.PropertyLocation, 'Molly')


    # testing total revenue method
    def test_Total_revenue(self):
        Property1 = Property('Kigali', 67, 345654, False)
        self.assertEqual(Property1.TotalRevenue, 23158818)

    #negative test for total revenue
    def test_Negative_Total_revenue(self):
        Property1 = Property('Kigali', 67, 345654, False)
        self.assertNotEqual(Property1.TotalRevenue, "Two hundred")

    def test_new_price(self):
        Property1 = Property('Kigali', 67, 5638392, False)
        new_price=5638392
        self.price=new_price
        self.assertEqual(Property1.price, 5638392)




if __name__ == '__main__':
    unittest.main()
