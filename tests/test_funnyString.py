import unittest
from coe_6710110184.funnyString import funny_string

class Testfunny_string(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(funny_string("acxz"), "Funny")  
    
    def test_case_2(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")  
    
    def test_case_3(self):
        self.assertEqual(funny_string("a"), "Funny")  
    
    def test_case_4(self):
        self.assertEqual(funny_string("aa"), "Funny") 

    def test_case_5(self):
        self.assertEqual(funny_string("aibohphobia"), "Funny")

    def test_case_6(self):
        self.assertEqual(funny_string("lmnopa"), "Not Funny")
