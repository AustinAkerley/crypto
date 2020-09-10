#!/usr/bin/python3
# Title: Unit Test for Jacobi Symbol
# Creator: Austin Akerley
# Date Created: 09/09/2020
# Last Editor: Austin Akerley
# Date Last Edited: 09/09/2020
# Associated Book Page Nuber: 175

import unittest
from crypto.src.jacobi_symbol import jacobi_symbol

class TestJacobiSymbol(unittest.TestCase):
    def test_jacobi_symbol_1(self): # Book example
        print("\n\nRunning test for src module: jacobi_symbol")
        a = 228530738017
        b = 9365449244297
        self.assertEqual(jacobi_symbol(a, b), -1)

    def test_jacobi_symbol_2(self): # Book example
        a = 171337608
        b = 536134436237
        self.assertEqual(jacobi_symbol(a, b), -1)

    def test_jacobi_symbol_3(self): # Book example
        a = 12389
        b = 9365449244297
        self.assertEqual(jacobi_symbol(a, b), 1)


if __name__ == '__main__':
    unittest.main()
