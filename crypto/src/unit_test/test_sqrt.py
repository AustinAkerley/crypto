#!/usr/bin/python3
import unittest
from crypto.src.sqrt import mod_sqrt

class Test(unittest.TestCase):


    def test_mod_sqrt_1(self):

        modulus = 83
        x = 80
        a = (x * x) % modulus
        x = mod_sqrt(a, modulus)
        
        self.assertEqual(x, (3,80))
        
    def test_mod_sqrt_2(self):
        modulus = 83
        x = 3
        a = (x * x) % modulus
        x = mod_sqrt(a, modulus)
        
        self.assertEqual(x, (3, 80))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()