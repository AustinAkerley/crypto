#!/usr/bin/python3
# Title: Unit Test for Legendre Symbol
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 02/09/2020
# Associated Book Page Nuber: N/A

import unittest
from crypto.src.legendre_symbol import legendre_symbol

class TestLegendreSymbol(unittest.TestCase):
    def test_legendre_symbol_1(self):
        print("\n\nRunning test for src module: legendre_symbol")
        p = 83
        a = 80
        expected = -1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_2(self):
        p = 83
        a = 7
        expected = 1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_3(self):
        p = 97
        a = 5
        expected = -1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_4(self):
        p = 97
        a = 72
        expected = 1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_5(self):
        p = 269
        a = 247
        expected = -1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_6(self):
        p = 269
        a = 248
        expected = 1
        self.assertEqual(legendre_symbol(a, p), expected)

    def test_legendre_symbol_7(self):
        p = 269
        a = 0
        expected = 0
        self.assertEqual(legendre_symbol(a, p), expected)

if __name__ == '__main__':
    unittest.main()
