#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_string = ''
    
for i in range (0, m) :
    for j in range (0, n) :
        matrix_string += matrix[j][i]

print (re.sub("([A-Z,a-z])[^(A-Z,a-z)]+([A-Z,a-z])", "\\1 \\2", matrix_string))