import sys
import unittest
import os
from pathlib import Path
from crypto.src.unit_test.test_eea import TestEEA

print("Number of args: "+str(len(sys.argv)))
print("Arg list: "+str(sys.argv))
print("Arg type: "+str(type(sys.argv)))
for arg in sys.argv[1:]:
    if arg == "-l":
        print("\nThis is a list of viable args and how to use them, including input/output types and descriptions: \n")
        print("-rt: Regression Test")
        print("  This stands for regression test, it is a flag with no following arguments to iterate through all of the unit test in the package and execute them.")
        print("  Use case: python3 crypto -l")
        break;

    if arg == "-rt":
        resp = os.system("python3 -m unittest discover")
        if resp == 0:
            print("\n\n\n\n---------------------------")
            print("Regression Test: PASSED   |")
            print("---------------------------")
        else:
            print("\n\n\n\n---------------------------")
            print("Regression Test: FAILED   |")
            print("---------------------------")

    else:
        print("\nInvalid arg: "+str(arg))
        print("  Use the -l flag to list all valid command line args")
