import unittest
from leapYear import leapYear

class TestLeapYear(unittest.TestCase):
    def test_leapYear3(self):
        self.assertEqual(leapYear(3), False)

if __name__ == "__main__":
    unittest.main()