"""
author: mary
date: 23.06.20
title: 달려라 홍준
"""

from collections import deque

N, M = map(int, input().split())
array = list(map(int, input().split()))
maxD = deque([])

# [1 1 1] 3 2
for n in range(2*M-2):
    while maxD and maxD[-1][1] < array[n+1]:
        maxD.pop()
    maxD.append((n, array[n+1]))
    if maxD[0][0] == n - M:
        maxD.popleft()

    if n >= M-1:
        print(maxD[0][1], end=" ")