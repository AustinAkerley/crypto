#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 12/12/2019
#
from crypto.cryptanalysis.order import order
import time
import unittest

class TestOrder(unittest.TestCase):
    def test_order_1(self):
        generator = 9704
        modulus = 17389
        expected_order = 1242
        output_order = order(generator, modulus)["order"]
        self.assertEqual(output_order, expected_order)

    def test_order_2(self):
        generator = 2
        modulus = 3267000013
        expected_order = 1089000004
        output_order = order(generator, modulus)["order"]
        self.assertEqual(output_order, expected_order)

    def test_order_3(self):
        generator = 23378
        modulus = 2860486313
        expected_order = 2860486312
        output_order = order(generator, modulus)["order"]
        self.assertEqual(output_order, expected_order)

if __name__ == '__main__':
    unittest.main()
