import unittest
from fizzBuzz import fizzBuzz

class TestFizzBuzz(unittest.Testcase):
    def test_fizzBuzz(self):
        self.assert(fizzBuzz(3), 'Fizz')
    