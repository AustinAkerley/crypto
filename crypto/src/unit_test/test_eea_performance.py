#!/usr/bin/python3
# Title: Functional Unit Test for Extended Euclidean Algorithm
# Creator: Austin Akerley
# Date Created: 11/26/2019
# Last Editor: Austin Akerley
# Date Last Edited:01/18/2020

import unittest
from crypto.src.eea import eea #UUT
import random
import math
import time
import csv

class TestEEAPerformance(unittest.TestCase):
    def test_eea_performance_1(self): #prints a list of runtime duration to number of bits of x and y
        max_bits = 1024
        data_points_per_bit = 10
        runtimes = []
        for i in range(0, max_bits+1):
            x = random.randint((2**i)+1, 2**(i+1))
            y = random.randint((2**i)+1, 2**(i+1))
            start = time.time()
            eea(x,y)
            stop = time.time()
            runtime = (stop-start) * 1000000
            runtimes.append(runtime)
            print("X and Y Number of Bits: "+str(i))
            print("Runtime(ms): "+str(runtime))

        #results in csv format
        with open('eea_runtimes.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0, max_bits+1):
                csvwriter.writerow([str(runtimes[i])])






if __name__ == '__main__':
    unittest.main()
