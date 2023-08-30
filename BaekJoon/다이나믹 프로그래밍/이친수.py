"""
author: mary
date: 23.08.30
title: 이친수
"""

import sys
input = sys.stdin.readline

N = int(input())
result = [0] * (N+1)

def calculate(x):
    if x <= 2:
        result[x] = 1
        return
    result[x] = result[x-2] + result[x-1]

for i in range(1, N+1):
    calculate(i)
print(result[N])
