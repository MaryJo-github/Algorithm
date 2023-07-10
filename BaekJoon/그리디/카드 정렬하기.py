"""
author: mary
date: 23.07.10
title: 카드 정렬하기
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    heapq.heappush(array, int(input()))

result = 0
while len(array) > 1:
    x = heapq.heappop(array)
    y = heapq.heappop(array)
    result += x + y
    heapq.heappush(array, x + y)

print(result)