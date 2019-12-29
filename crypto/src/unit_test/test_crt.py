#!/usr/bin/python3
# Title: Unit Test for Chinese Remainder Theorem
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited: 12/28/2019
# Associated Book Page Nuber: XXXXXXXX
from crypto.src.crt import crt
import unittest

class TestCRT(unittest.TestCase):
    def test_crt_1(self):
        ax_px0 = (1,5) # x = 1 (mod 5)
        ax_px1 = (9, 11) # x = 9 (mod 11)
        equivalencies = [ax_px0, ax_px1]
        x = 31
        self.assertEqual(crt(equivalencies), x)

    def test_crt_2(self):
        ax_px0 = (2, 3) # x = 2 (mod 3)
        ax_px1 = (3, 7) # x = 3 (mod 7)
        ax_px2 = (4, 16) # x = 4 (mod 16)
        equivalencies = [ax_px0, ax_px1, ax_px2]
        x = 164
        self.assertEqual(crt(equivalencies), x)

    def test_crt_3(self):
        ax_px0 = (4196, 4423)
        ax_px1 = (345, 6917)
        equivalencies = [ax_px0, ax_px1]
        x = 6917345
        self.assertEqual(crt(equivalencies), x)

if __name__ == '__main__':
    unittest.main()
