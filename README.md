mean

The mean tool computes the arithmetic mean along the specified axis.
var

The var tool computes the arithmetic variance along the specified axis.

std

The std tool computes the arithmetic standard deviation along the 
specified axis.
Task

You are given a 2-D array of size NXM.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None

import numpy as np
N, _ = map(int, input().split())

arr = np.array([list(map(int, input().split())) for _ in range(N)])

print(np.mean(arr, axis=1), np.var(arr, axis=0), round(np.std(arr),11), sep='\n')
