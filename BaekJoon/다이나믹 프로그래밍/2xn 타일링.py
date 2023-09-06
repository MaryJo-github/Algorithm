"""
author: mary
date: 23.09.03
title: 2xn 타일링
"""

import sys
input = sys.stdin.readline

n = int(input())
array = [0] * (n+1)
array[0] = 1
array[1] = 1

for i in range(2, n+1):
    if i == 2:
        array[i] = 2
        continue
    array[i] = 2 * array[i-1] - array[i-3]

print(array[n] % 10007)