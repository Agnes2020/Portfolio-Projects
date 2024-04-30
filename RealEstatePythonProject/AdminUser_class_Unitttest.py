#Author: Agnes Fusese
import unittest
from AdminUser_class import MainUser

# __init__test

class TestStringMethods(unittest.TestCase):
    def test_init(self):
        MainUser1 = MainUser("Agnes","Doreen")
        self.assertEqual(MainUser1.password, 'Agnes')

    # negative _init_ test
    def test_Negative_init(self):
        MainUser1 = MainUser("Agnes", "Doreen")
        self.assertNotEqual(MainUser1.password, 'Doreen')

    # testing account creation method
    def test_set_user_name_and_password(self):
        UserCredentials= MainUser('Agnes',"Doreen")
        self.assertEqual(UserCredentials.username,"Doreen")

    # negative account creation test
    def test_Negative_set_user_name_and_password(self):
        UserCredentials= MainUser('Agnes',"Doreen")
        self.assertNotEqual(UserCredentials.username,"Jonah")

if __name__ == '__main__':
    unittest.main()