"""
author: mary
date: 23.07.09
title: 동전 0
"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
array = [int(input()) for _ in range(N)]

result = 0
for n in range(N-1,-1,-1):
    result += K // array[n]
    K %= array[n]
print(result)