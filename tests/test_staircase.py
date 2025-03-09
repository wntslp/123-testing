import unittest
from coe_6710110184.Staircase import staircase

class TestStaircase(unittest.TestCase):
    def test_staircase_size_4_with_default_char(self):
        n = 4
        expected_output = "   #\n  ##\n ###\n####"
        result = staircase(n)  
        self.assertEqual(result, expected_output)

    def test_staircase_size_5_with_custom_char(self):
        n = 5
        char = "*"
        expected_output = "    *\n   **\n  ***\n ****\n*****"
        result = staircase(n, char)
        self.assertEqual(result, expected_output)

    def test_staircase_size_1(self):
        n = 1
        expected_output = "#"
        result = staircase(n)
        self.assertEqual(result, expected_output)

    def test_invalid_n_too_large(self):
        with self.assertRaises(ValueError):
            staircase(31)

    def test_invalid_n_too_small(self):
        with self.assertRaises(ValueError):
            staircase(0)

    def test_staircase_size_3(self):
        n = 3
        expected_output = "  #\n ##\n###"
        result = staircase(n)  
        self.assertEqual(result, expected_output)

    def test_staircase_with_space_char(self):
        n = 3
        char = " "
        expected_output = "     \n    \n   "
        result = staircase(n, char)
        self.assertEqual(result, expected_output)

    def test_invalid_n_type(self):
        with self.assertRaises(TypeError):
            staircase("5")

    def test_invalid_char_type(self):
        with self.assertRaises(TypeError):
            staircase(5, 3)