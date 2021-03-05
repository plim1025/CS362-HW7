import unittest
from leapYear import leapYear

class TestLeapYear(unittest.TestCase):
    def test_leapYear3(self):
        self.assertEqual(leapYear(3), False)
    def test_leapYear16(self):
        self.assertEqual(leapYear(16), True)
    def test_leapYear400(self):
        self.assertEqual(leapYear(400), True)
    def test_leapYear300(self):
        self.assertEqual(leapYear(300), False)

if __name__ == "__main__":
    unittest.main()