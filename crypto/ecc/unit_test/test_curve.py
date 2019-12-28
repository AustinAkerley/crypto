#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 12/09/2019
#
from crypto.ecc.curve import curve
import unittest

class TestCurve(unittest.TestCase):
    def test_curve_1(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        Q = (1,8)
        expected_R = (2, 10)
        R = my_curve.add(P, Q)
        print("R: " + str(R))
        self.assertEqual(R, expected_R)

    def test_curve_2(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        P2 = my_curve.add(P, P)
        expected_P2 = (9,6)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_3(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        Q = (None, None)
        R = my_curve.add(P, Q)
        expected_R = P
        print("R: " + str(R))
        self.assertEqual(R, expected_R)

    def test_curve_multiply_1(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        P2 = my_curve.multiply(P, 2)
        expected_P2 = (9,6)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_multiply_1(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        P2 = my_curve.multiply(P, 5)
        expected_P2 = (8,6)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

if __name__ == '__main__':
    unittest.main()
