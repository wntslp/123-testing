from coe_6710110184.grid_challenge import gridChallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_sorted_grid(self):
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")

    def test_unsorted_grid(self):
        self.assertEqual(gridChallenge(["zxy", "bca", "lmn"]), "NO")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["abcdef"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")

    def test_single_element(self):
        self.assertEqual(gridChallenge(["a"]), "YES")

    def test_same_elements(self):
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")

    def test_mix_elements(self):
        self.assertEqual(gridChallenge(["acb", "bda", "cfe"]), "YES")

    def test_case_sensitivity(self):
        self.assertEqual(gridChallenge(["Abc", "Def", "Ghi"]), "YES") 