#!/usr/bin/python3
# Title: Unit Test for Quadratic Reciprocity
# Creator: Austin Akerley
# Date Created: 09/09/2020
# Last Editor: Austin Akerley
# Date Last Edited: 09/09/2020
# Associated Book Page Nuber: 175

import unittest
from crypto.src.quadratic_reciprocity import quadratic_reciprocity

class TestQuadraticReciprocity(unittest.TestCase):
    def test_quadratic_reciprocity_1(self): # Book example
        print("\n\nRunning test for src module: quadratic_reciprocity")
        a = 228530738017
        b = 9365449244297
        self.assertEqual(quadratic_reciprocity(a, b), -1)

    def test_quadratic_reciprocity_2(self): # Book example
        a = 171337608
        b = 536134436237
        self.assertEqual(quadratic_reciprocity(a, b), -1)

    def test_quadratic_reciprocity_3(self): # Book example
        a = 12389
        b = 9365449244297
        self.assertEqual(quadratic_reciprocity(a, b), 1)


if __name__ == '__main__':
    unittest.main()
