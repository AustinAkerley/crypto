#!/usr/bin/python3
# Title: Unit Test for Has Square Root
# Creator: Austin Akerley
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited: 12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import unittest
from crypto.src.has_sqrt import has_sqrt

class TestHasSqrt(unittest.TestCase):
    def test_has_sqrt_1(self):
        p = 83
        a = 80
        expected = False
        self.assertEqual(has_sqrt(a, p), expected)

    def test_has_sqrt_2(self):
        p = 83
        a = 7
        expected = True
        self.assertEqual(has_sqrt(a, p), expected)

    def test_has_sqrt_3(self):
        p = 97
        a = 5
        expected = False
        self.assertEqual(has_sqrt(a, p), expected)

    def test_has_sqrt_4(self):
        p = 97
        a = 72
        expected = True
        self.assertEqual(has_sqrt(a, p), expected)

if __name__ == '__main__':
    unittest.main()
