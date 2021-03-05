import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzBuzz3(self):
        self.assertEqual(fizzBuzz(3), 'Fizz')
    def test_fizzBuzz5(self):
        self.assertEqual(fizzBuzz(5), 'Buzz')
    
