"""
author: mary
date: 23.07.05
title: K번째 수
"""

import sys
input = sys.stdin.readline
N = int(input())
k = int(input())

def count_less(num):
    cnt = 0
    for r in range(1, N+1):
        cnt += min(N, (num-1)//r)
    return cnt

answer = 0
L, R = 1, N*N
while L <= R:
    mid = (L+R)//2
    cnt = count_less(mid)
    if cnt <= k-1:
        answer = max(answer, mid)
        L = mid+1
    elif cnt > k-1:
        R = mid-1
print(answer)