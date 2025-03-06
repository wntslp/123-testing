from coe_6710110184.two_characters import alternate
import unittest

class TestTwoCharacters(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)  # "bababa" (6 ตัว)

    def test_all_same_character(self):
        self.assertEqual(alternate("aaaaaaa"), 0)  # ไม่มีคู่ที่ต่างกัน

    def test_no_valid_pair(self):
        self.assertEqual(alternate("abcd"), 2)  # เช่น "ab" หรือ "ac"

    def test_already_alternating(self):
        self.assertEqual(alternate("abababab"), 8)  # ใช้ได้ทั้ง string

    def test_only_two_characters(self):
        self.assertEqual(alternate("baba"), 4)  # "baba" ถูกต้องอยู่แล้ว

    def test_large_input(self):
        self.assertEqual(alternate("a" * 1000), 0)

    def test_mixed_case(self):
        self.assertEqual(alternate("aAaAaA"), 6)  # ควรใช้ case-sensitive → "aAaAaA" ถูกต้อง

    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)  # สตริงว่าง ผลลัพธ์ต้องเป็น 0
