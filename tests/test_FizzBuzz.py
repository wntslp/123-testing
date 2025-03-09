from coe_6710110184.FizzBuzz import fizzbuzz

import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_should_return_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_give_5_should_return_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_give_15_should_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_give_7_should_return_7(self):
        self.assertEqual(fizzbuzz(7), "7") 

    def test_give_30_should_return_fizzbuzz(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")