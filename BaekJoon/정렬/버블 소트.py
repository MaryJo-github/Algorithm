"""
author: mary
date: 23.07.15
title: 버블 소트
"""
import sys
input = sys.stdin.readline
N = int(input())
A = [(0,0)]
[A.append((int(input()), n+1)) for n in range(N)]
A.sort()

max = 0
for k in range(1, N+1):
    if max < A[k][1]-k:
        max = A[k][1]-k

print(max+1)