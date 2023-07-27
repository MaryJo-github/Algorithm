"""
author: mary
date: 23.07.27
title: 최소공배수
"""
import sys
input = sys.stdin.readline
T = int(input())
array = [list(map(int, input().split())) for _ in range(T)]

def 최대공약수(a, b):
    if b == 0:
        return a
    return 최대공약수(b, a%b)

def 최소공배수(x, y):
    k = 최대공약수(x, y)
    return k * (x//k) * (y//k)

for t in range(T):
    print(최소공배수(array[t][0], array[t][1]))
    