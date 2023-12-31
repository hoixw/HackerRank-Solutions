#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

## List Slicing method
def reverseArray(a):
    return a[::-1]

## Using arr.reverse()
def reverseArray2(a):
    a.reverse()
    return a
    
# In place swap     
def ReverseArray3(a):
    for i in range(0, len(a)//2):
        a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
        
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
