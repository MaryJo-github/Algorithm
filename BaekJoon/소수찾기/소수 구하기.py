"""
author: mary
date: 23.06.23
title: 소수 구하기
"""

# M, N = map(int, input().split())

# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True

# for k in range(M, N+1):
#     if isPrime(k):
#         print(k)

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
true_false_list = [True] * (N+1)
true_false_list[1] = False

for i in range(2, int(N**0.5) + 1):
    if true_false_list[i] == True:
        for j in range(2 * i, N+1, i):
            true_false_list[j] = False

for i in range(M, N+1):
    if true_false_list[i]:
        print(i)