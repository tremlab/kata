import unittest
import roman.num


class RomanToArabic(unittest.TestCase):
    """integration test"""
    def test_x_is_10(self):
        self.assertEqual(roman_num.convert("X"), 10)

    def test_xi_is_11(self):
        self.assertEqual(roman_num.convert("XI"), 11)

    def test_ix_is_9(self):
        self.assertEqual(roman_num.convert("IX"), 9)

    def test_MMDCLXVI_is_2666(self):
        self.assertEqual(roman_num.convert("MMDCLXVI"), 2666)

    def test_CMXLIV_is_944(self):
        self.assertEqual(roman_num.convert("CMXLIV"), 944)
     

if __name__ == "__main__":
    unittest.main()