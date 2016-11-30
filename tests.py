import unittest
from primenumbers import prime_numbers

#test case is created by subclassing unittest.TestCase
class Testprimenumbers(unittest.TestCase):

    #function for checking if the number is a negative number
    def test_negative_numbers(self):
        self.assertEqual(prime_numbers(-1) , "You cannot enter negative numbers")

    #function to check if the numbers generated are actually primenumbers
    def test_prime_numbers(self):
        self.assertEqual(prime_numbers(5) , [2 , 3 ,5])
