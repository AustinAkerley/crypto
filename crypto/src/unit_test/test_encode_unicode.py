#!/usr/bin/python3
# Author: Austin Akerley
# Date Last Edited: 10/31/2019
#
from crypto.src.encode_unicode import encode_unicode
import unittest

class TestEncodeUnicode(unittest.TestCase):
    def test_encode_unicode_1(self):
        message = "a"
        result = 97
        self.assertEqual(encode_unicode(message), result)

    def test_encode_unicode_2(self):
        message = None
        result = None
        self.assertEqual(encode_unicode(message), result)

    def test_encode_unicode_3(self):
        message = "Once upon a time in a forest long ago"
        result = [79, 110, 99, 101, 32, 117, 112, 111, 110, 32, 97, 32, 116, 105, 109, 101, 32, 105, 110, 32, 97, 32, 102, 111, 114, 101, 115, 116, 32, 108, 111, 110, 103, 32, 97, 103, 111]
        self.assertEqual(encode_unicode(message), result)

    def test_encode_unicode_4(self):
        message = "The Germans are pushing in from the South, send backup."
        result = [84, 104, 101, 32, 71, 101, 114, 109, 97, 110, 115, 32, 97, 114, 101, 32, 112, 117, 115, 104, 105, 110, 103, 32, 105, 110, 32, 102, 114, 111, 109, 32, 116, 104, 101, 32, 83, 111, 117, 116, 104, 44, 32, 115, 101, 110, 100, 32, 98, 97, 99, 107, 117, 112, 46]
        self.assertEqual(encode_unicode(message), result)

if __name__ == '__main__':
    unittest.main()
