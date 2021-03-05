import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzBuzz3(self):
        self.assertEqual(fizzBuzz(3), 'Fizz')
    def test_fizzBuzz5(self):
        self.assertEqual(fizzBuzz(5), 'Buzz')
    def test_fizzBuzz15(self):
        self.assertEqual(fizzBuzz(15), 'FizzBuzz')
    def test_fizzBuzz4(self):
        self.assertEqual(fizzBuzz(4), 4)
