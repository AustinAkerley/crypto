#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from crypto.src.mod_inv import mod_inv
import unittest

class TestModInv(unittest.TestCase):
    def test_mod_inv_1(self):
        a = 5
        m = 7
        b = 3
        self.assertEqual(mod_inv(a, m), b)

    def test_mod_inv_2(self):
        a = 3
        m = 7
        b = 5
        self.assertEqual(mod_inv(a, m), b)

    def test_mod_inv_3(self):
        a = 632
        m = 999749
        b = 93331
        self.assertEqual(mod_inv(a, m), b)

    def test_mod_inv_4(self):
        a = 173920
        m = 100207
        b = 5541
        self.assertEqual(mod_inv(a, m), b)

    def test_mod_inv_5(self):
        a = 0
        m = 7
        b = 0
        self.assertEqual(mod_inv(a, m), b)

if __name__ == '__main__':
    unittest.main()