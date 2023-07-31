#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# This is a very cool problem
## The best approach is to use a cumulative sum, rather than actually calculating
## The relevant totals
## We add query[2] at query[1], and then subtract at query[1]+1, indicating that the running
## Total has changed. We can then run through the arr and figure out the max.

def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    for query in queries:
        arr[query[0] - 1] += query[2]
        arr[query[1]] -= query[2]
    
    running_total, maxval = 0, 0
    
    for item in arr:
        running_total += item
        maxval = max(maxval, running_total)
    
    return maxval

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
