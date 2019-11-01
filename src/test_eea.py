#!/usr/bin/python3
import eea
import unittest

class TestEEA(unittest.TestCase):
    def test_eea_1(self):
        x = 140
        y = 21
        self.assertEqual(eea.eea(x, y), [7, -1, 140, 7, 21])
    def test_eea_2(self):
        x = 3
        y = 21
        self.assertEqual(eea.eea(x, y), [3, 0, 21, 1, 3])
    def test_eea_3(self):
        x = 63451367846845
        y = 52352467468873425
        self.assertEqual(eea.eea(x, y), [5, -5224108618601, 52352467468873425, 4310308599955094, 63451367846845])
    def test_eea_4(self):
        x = 0
        y = 0
        self.assertEqual(eea.eea(x, y), [0, 0, 0, 0, 0])
    def test_eea_5(self):
        x = 5
        y = 0
        self.assertEqual(eea.eea(x, y), [0, 0, 0, 0, 0])
    def test_eea_6(self):
        x = 0
        y = 11
        self.assertEqual(eea.eea(x, y), [0, 0, 0, 0, 0])
    def test_eea_7(self):
        x = 999749
        y = 100207
        self.assertEqual(eea.eea(x, y), [1, 12650, 999749, -126207, 100207])
if __name__ == '__main__':
    unittest.main()
