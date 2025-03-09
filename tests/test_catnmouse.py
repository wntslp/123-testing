from coe_6710110184.catnmouse import catnmouse

import unittest

class TestCatnMouse(unittest.TestCase):
    def test_catnmouse_cat_a(self):
        # Arrange
        x = 1
        y = 2
        z = 3
        expected_output = "Cat A"
        
        # Act
        result = catnmouse(x, y, z)  

        # Assert
        self.assertEqual(result, expected_output)