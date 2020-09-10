#!/usr/bin/python3
# Title: Unit Test for Calculating the Order of a Generator in Fp or the field of the modulus
# Creator: Austin Akerley
# Date Created: 12/25/2019
# Last Editor: Austin Akerley
# Date Last Edited:12/28/2019
# Associated Book Page Nuber: XXXXXXXX

import time
import unittest
from crypto.cryptanalysis.order import order

class TestOrder(unittest.TestCase):
    def test_order_functional_1(self):
        print("\n\nRunning test for cryptanalysis module: order")
        generator = 9704
        modulus = 17389
        expected_order = 1242
        output_order = order(generator, modulus)
        self.assertEqual(output_order, expected_order)

    def test_order_functional_2(self):
        generator = 2
        modulus = 3267000013
        expected_order = 1089000004
        output_order = order(generator, modulus)
        self.assertEqual(output_order, expected_order)

    def test_order_functional_3(self):
        generator = 23378
        modulus = 2860486313
        expected_order = 2860486312
        output_order = order(generator, modulus)
        self.assertEqual(output_order, expected_order)

    def test_order_functional_4(self):
        generator = 3
        modulus = 7
        expected_order = 6
        output_order = order(generator, modulus)
        self.assertEqual(output_order, expected_order)

    def test_order_functional_5(self):
        generator = 37
        modulus = 839
        expected_order = 419
        output_order = order(generator, modulus)
        self.assertEqual(output_order, expected_order)

    def test_order_functional_6(self):
        generator = 1
        modulus = 2
        expected_order = 1
        output_order = order(generator, modulus)
        self.assertEqual(output_order, expected_order)

if __name__ == '__main__':
    unittest.main()
