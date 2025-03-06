from coe_6710110184.caesar_cipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_case_2(self):
        self.assertEqual(caesarCipher("Hello_World!", 4), "Lipps_Asvph!")

    def test_case_3(self):
        self.assertEqual(caesarCipher("A", 1), "B")

    def test_case_4(self):
        self.assertEqual(caesarCipher("Z", 1), "A")

    def test_case_5(self):
        self.assertEqual(caesarCipher("a", 1), "b")

    def test_case_6(self):
        self.assertEqual(caesarCipher("z", 1), "a")

    def test_case_7(self):
        self.assertEqual(caesarCipher("a", 26), "a")