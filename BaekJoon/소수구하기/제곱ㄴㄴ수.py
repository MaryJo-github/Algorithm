"""
author: mary
date: 23.07.24
title: 제곱ㄴㄴ수
"""
import sys
input = sys.stdin.readline

min, max = list(map(int, input().split()))
제곱수 = [i**2 for i in range(2, int(max**0.5)+1)]
array = [1] * (max-min+1)

for i in 제곱수:
    n = (min//i) * i
    while n <= max:
        if n - min >= 0:
            array[n-min] = 0
        n += i

print(sum(array))