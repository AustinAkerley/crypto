#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from crypto.src.eea import eea
import unittest

class TestEEA(unittest.TestCase):
    def test_eea_1(self):
        x = 140
        y = 21
        self.assertEqual(eea(x, y), {"gcd":7, "a":-1, "x":140, "b":7, "y":21})
    def test_eea_2(self):
        x = 3
        y = 21
        self.assertEqual(eea(x, y),{"gcd":3, "a":1, "x":3, "b":0, "y":21})
    def test_eea_3(self):
        x = 63451367846845
        y = 52352467468873425
        self.assertEqual(eea(x, y), {"gcd":5, "a":4310308599955094, "x":63451367846845, "b":-5224108618601, "y":52352467468873425})
    def test_eea_4(self):
        x = 0
        y = 0
        self.assertEqual(eea(x, y), {"gcd":0, "a":0, "x":0, "b":0, "y":0})
    def test_eea_5(self):
        x = 5
        y = 0
        self.assertEqual(eea(x, y), {"gcd":0, "a":0, "x":0, "b":0, "y":0})
    def test_eea_6(self):
        x = 0
        y = 11
        self.assertEqual(eea(x, y), {"gcd":0, "a":0, "x":0, "b":0, "y":0})
    def test_eea_7(self):
        x = 999749
        y = 100207
        self.assertEqual(eea(x, y), {"gcd":1, "a":12650, "x":999749, "b":-126207, "y":100207})
if __name__ == '__main__':
    unittest.main()