#!/usr/bin/python3
import eea
import unittest

class TestEEA(unittest.TestCase):
    def test_eea(self):
        self.assertEqual(eea.eea(0,0), [0,0,0,0])

if __name__ == '__main__':
    unittest.main()
