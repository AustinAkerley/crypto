#!/usr/bin/python3
# Title: Brute Force Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import unittest
from crypto.ecc.curve import curve

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

    def test_curve_multiply_2(self):
        my_curve = curve(14,19,3623)
        P = (6,730)
        P2 = my_curve.multiply(P, 947)
        expected_P2 = (3492,60)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_multiply_3(self):
        my_curve = curve(8,7,73)
        P = (32,53)
        P2 = my_curve.multiply(P, 11)
        expected_P2 = (39,17)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)
    
    def test_curve_point_convert(self):
        my_curve = curve(14,19,3623)
        msg = 34
        P = my_curve.msg_to_point(msg)
        self.assertEqual(msg, my_curve.point_to_msg(P))

if __name__ == '__main__':
    unittest.main()
