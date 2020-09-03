#!/usr/bin/python3
# Title: Unit Test for Primality Test
# Creator: Austin Akerley
# Date Created: 04/04/2020
# Last Editor: Austin Akerley
# Date Last Edited: 04/04/2020
# Associated Book Page Nuber: N/A

import unittest
from crypto.src.primality_test import primality_test

class TestPrimalityTest(unittest.TestCase):
    def test_primality_test_1(self):
        print("\n\nRunning test for src module: primality_test")
        certainty = 1000
        n = 13
        expected_is_prime = True
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)

    def test_primality_test_2(self):
        certainty = 1000
        n = 32497
        expected_is_prime = True
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)

    def test_primality_test_3(self):
        certainty = 1000
        n = 17
        expected_is_prime = True
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)

    def test_primality_test_4(self):
        certainty = 1000
        n = 18672340963
        expected_is_prime = False
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)

    def test_primality_test_5(self):
        certainty = 1000
        n = 28116440335967
        expected_is_prime = True
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)

    def test_primality_test_6(self):
        certainty = 1000
        n = 13790129586234798731
        expected_is_prime = False
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)

    def test_primality_test_7(self):
        certainty = 1000
        n = 99999999999991
        expected_is_prime = False
        is_prime  = primality_test(n, certainty)
        print("Expected to be "+str(expected_is_prime) + " | Was actually "+str(is_prime))
        self.assertEqual(expected_is_prime, is_prime)



if __name__ == '__main__':
    unittest.main()
