"""
author: mary
date: 23.06.21
title: 오큰수
"""

N = int(input())
A = list(map(int, input().split()))
stack = []
result = [-1 for i in range(N)]

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)