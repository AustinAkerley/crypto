#!/usr/bin/python3
# Title: Unit Test for Prime Number Theorem
# Creator: Austin Akerley
# Date Created: 04/04/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/04/2020
# Associated Book Page Nuber: 133

import unittest
from crypto.src.prime_number_theorem import prime_number_theorem

class TestPrimalityTest(unittest.TestCase):
    def test_primality_test_1(self):
        prime_number_theorem(50001)


if __name__ == '__main__':
    unittest.main()
