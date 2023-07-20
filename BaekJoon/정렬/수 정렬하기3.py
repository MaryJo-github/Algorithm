"""
author: mary
date: 23.07.20
title: 수 정렬하기3
"""
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# array = []
# max_digit = 0
# for _ in range(N):
#     a = input().rstrip()
#     array.append(a)
#     if max_digit < len(a):
#         max_digit = len(a)
    
# number_deque = [deque() for _ in range(N)]

# for i in range(max_digit):
#     for element in array:
#         if len(element) < max_digit:
#             value = 0
#         else:
#             value = element[i-1]
#         number_deque[int(element[i])].append(element)
#     array_tmp = []
#     for j in range(10):
#         while number_deque[j]:
#             array_tmp.append(number_deque[j].popleft())
#     array = array_tmp
# print(*array, sep = "\n")


import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numbers = [0] * 10001

for _ in range(N):
    numbers[int(input())] += 1

for n in range(10001):
    while numbers[n] > 0:
        print(n)
        numbers[n] -= 1
