#!/usr/bin/python3
# Title: Unit Test for Modular Multiplicative Inverse
# Creator: Austin Akerley
# Date Created: 12/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: N/A

import unittest
from crypto.src.mod_inv import mod_inv

class TestModInv(unittest.TestCase):
    def test_mod_inv_1(self):
        print("\n\nRunning test for src module: mod_inv")
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
        with self.assertRaises(ValueError):
            self.assertEqual(mod_inv(a, m), b)

if __name__ == '__main__':
    unittest.main()
