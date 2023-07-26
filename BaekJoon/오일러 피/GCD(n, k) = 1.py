"""
author: mary
date: 23.07.26
title: GCD(n, k) = 1
"""
import sys
input = sys.stdin.readline
n = int(input())

array = [1] * (n+1)
array[0] = 0

for i in range(2, n+1):
    if array[i] == 1:
        if n % i == 0:
            k = i
            while k <= n:
                array[k] = 0
                k += i
print(sum(array))

