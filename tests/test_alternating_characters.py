from coe_6710110184.alternating_characters import alternating_characters

import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(alternating_characters("AAAA"), 3)

    def test_case_2(self):
        self.assertEqual(alternating_characters("BBBBB"), 4)

    def test_case_3(self):
        self.assertEqual(alternating_characters("ABABABAB"), 0)

    def test_case_4(self):
        self.assertEqual(alternating_characters("BABABA"), 0)

    def test_case_5(self):
        self.assertEqual(alternating_characters("AAABBB"), 4)

    def test_case_6(self):
        self.assertEqual(alternating_characters("A"), 0)

    def test_case_7(self):
        self.assertEqual(alternating_characters("AB"), 0)

    def test_case_8(self):
        self.assertEqual(alternating_characters("ABBABB"), 2)

    def test_case_9(self):
        self.assertEqual(alternating_characters("BBBBBAAB"), 5)

    def test_case_10(self):
        self.assertEqual(alternating_characters("AABBAABB"), 4)