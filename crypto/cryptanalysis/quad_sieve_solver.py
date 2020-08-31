#!/usr/bin/python3
# Title: Quadratic Sieve Client
# Creator: Austin Akerley
# Date Created: 08/02/2020
# Last Editor: Austin Akerley
# Date Last Edited: 08/02/2020
# Associated Book Page Nuber: 143

import json
print("LOADING JSON")
entries = None
with open("entries_1.json") as f:
    entries = json.load(f)
print("FINISHED LOADING JSON")

list_of_arrays = []
list_of_x = []
for matrix in entries:
    print(matrix)
    array = []
    for ele in matrix:
        array.append(int(ele))
    print("LEN : "+str(len(array)))
    list_of_arrays.append(array)
    list_of_x.append(entries.get(matrix))
