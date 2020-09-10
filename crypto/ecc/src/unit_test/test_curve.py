#!/usr/bin/python3
# Title: Brute Force Elliptic Curve Discrete Logarithm
# Creator: Daniel Gerthe
# Date Created: 12/28/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: 299

import unittest
from crypto.ecc.src.curve import curve

class TestCurve(unittest.TestCase):
    def test_curve_add_functional_1(self):
        print("\n\nRunning test for ecc src module: curve")
        my_curve = curve(3,8,13)
        P = (9,7)
        Q = (1,8)
        expected_R = (2, 10)
        R = my_curve.add(P, Q)
        print("R: " + str(R))
        self.assertEqual(R, expected_R)

    def test_curve_add_functional_2(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        P2 = my_curve.add(P, P)
        expected_P2 = (9,6)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_add_functional_3(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        Q = (None, None)
        R = my_curve.add(P, Q)
        expected_R = P
        print("R: " + str(R))
        self.assertEqual(R, expected_R)

    def test_curve_multiply_functional_1(self):
        my_curve = curve(3,8,13)
        P = (9,7)
        P2 = my_curve.multiply(P, 2)
        expected_P2 = (9,6)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_multiply_functional_2(self):
        my_curve = curve(14,19,3623)
        P = (6,730)
        P2 = my_curve.multiply(P, 947)
        expected_P2 = (3492,60)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_multiply_functional_3(self):
        my_curve = curve(8,7,73)
        P = (32,53)
        P2 = my_curve.multiply(P, 11)
        expected_P2 = (39,17)
        print("P2: " + str(P2))
        self.assertEqual(P2, expected_P2)

    def test_curve_is_point_on_curve_functional_1(self):
        my_curve = curve(14,19,3623)
        P = (6,730)
        Q = P
        points = []
        points.append(Q)
        for i in range (1,3623):
            Q = my_curve.add(P, Q)
            points.append(Q)

    def test_curve_is_point_on_curve_functional_2(self):
        my_curve = curve(14,19,3623)
        P = (6,730)
        Q = (3513, 2669)
        on_curve = my_curve.is_point_on_curve(Q)
        expected_on_curve = True
        self.assertEqual(on_curve, expected_on_curve)

    def test_curve_is_point_on_curve_functional_3(self):
        my_curve = curve(14,19,3623)
        P = (6,730)
        Q = (3513, 2668)
        on_curve = my_curve.is_point_on_curve(Q)
        expected_on_curve = False
        self.assertEqual(on_curve, expected_on_curve)

    def test_curve_is_point_on_curve_functional_4(self):
        my_curve = curve(14,19,3623)
        P = (6,730)
        Q = (3, 345)
        on_curve = my_curve.is_point_on_curve(Q)
        expected_on_curve = False
        self.assertEqual(on_curve, expected_on_curve)


if __name__ == '__main__':
    unittest.main()
