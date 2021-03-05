import unittest
from leapYear import leapYear

class TestLeapYear(unittest.TestCase):
    def test_leapYear3(self):
        self.assertEqual(leapYear(3), False)
    def test_leapYear400(self):
        self.assertEqual(leapYear(400), True)

if __name__ == "__main__":
    unittest.main()