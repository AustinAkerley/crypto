#!/usr/bin/python3
# Title: Unit Test for Has Square Root
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 01/19/2020
# Associated Book Page Nuber: N/A

import unittest
from crypto.src.legendre_symbol import legendre_symbol

class TestLegendreSymbol(unittest.TestCase):
    def test_legendre_symbol_functional_1(self):
        p = 83
        a = 80
        expected = -1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_functional_2(self):
        p = 83
        a = 7
        expected = 1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_functional_3(self):
        p = 97
        a = 5
        expected = -1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_functional_4(self):
        p = 97
        a = 72
        expected = 1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_functional_5(self):
        p = 269
        a = 247
        expected = -1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_functional_6(self):
        p = 269
        a = 248
        expected = 1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_functional_5(self):
        p = 269
        a = 0
        expected = 0
        self.assertEqual(legendre_symbol(a, p), expected)

if __name__ == '__main__':
    unittest.main()