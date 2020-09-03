#!/usr/bin/python3
# Title: Unit Test for Pollard's p-1 Factorization Algorithm
# Creator: Austin Akerley
# Date Created: 05/17/2020
# Last Editor: Austin Akerley
# Date Last Edited: 05/17/2020
# Associated Book Page Nuber: 139

import unittest
from crypto.cryptanalysis.pollard import pollard

class TestPollard(unittest.TestCase):
    def test_pollard_1(self):
        print("\n\nRunning test for cryptanalysis module: pollard")
        N = 13927189
        p = pollard(N)
        expected_p = 3823
        print("p: "+str(p))
        self.assertEqual(expected_p, p)

    def test_pollard_2(self):
        N = 168441398857
        p = pollard(N)
        expected_p = 350437
        print("p: "+str(p))
        self.assertEqual(expected_p, p)


if __name__ == '__main__':
    unittest.main()
