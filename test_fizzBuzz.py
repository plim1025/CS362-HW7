import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.Testcase):
    def test_fizzBuzz3(self):
        self.assertEqual(fizzBuzz(3), 'Fizz')
    
