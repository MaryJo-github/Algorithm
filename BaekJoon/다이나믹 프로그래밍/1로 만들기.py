"""
author: mary
date: 23.08.28
title: 1로 만들기
"""

import sys
input = sys.stdin.readline
N = int(input())

array = [0] * (N + 1)

for i in range(2, N + 1):
    array[i] = array[i-1]+1
    if i % 3 == 0:
        array[i] = min(array[i], array[i//3] + 1)
    if i % 2 == 0:
        array[i] = min(array[i], array[i//2] + 1)

print(array[N])


### 필요한 계산만 하기 때문에 top down 방식이 더 빠름
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())

# dp = {1: 0}

# def top_down(n):
#     if n in dp.keys():
#         return dp[n]
#     if (n % 3 == 0) and (n % 2 == 0):
#         dp[n] = min(top_down(n // 3) + 1, top_down(n // 2) + 1)
#     elif n % 3 == 0:
#         dp[n] = min(top_down(n // 3) + 1, top_down(n - 1) + 1)
#     elif n % 2 == 0:
#         dp[n] = min(top_down(n // 2) + 1, top_down(n - 1) + 1)
#     else:
#         dp[n] = top_down(n - 1) + 1
#     return dp[n]

# print(top_down(N))