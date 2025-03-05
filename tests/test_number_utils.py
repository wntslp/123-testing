from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_6_8_is_not_prime(self):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_1_2_3_4_5_is_not_prime(self):
        prime_list = [1, 2, 3, 4, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_101_103_107_is_prime(self):
        prime_list = [101, 103, 107]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_empty_list_is_not_prime(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)