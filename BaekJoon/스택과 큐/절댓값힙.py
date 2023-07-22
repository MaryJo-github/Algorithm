"""
author: mary
date: 23.06.22
title: 절댓값힙
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
queue = []
result = []

for _ in range(N):
    v = int(input())
    if v == 0:
        try:
            print(heapq.heappop(queue)[1])
        except:
            print(0)
    else:
        heapq.heappush(queue, (abs(v),v))

# import heapq

# N = int(input())
# heap = []
# result = []

# for n in range(N):
#     a = int(input())
#     if a == 0:
#         if len(heap) == 0:
#             result.append(0)
#             continue
#         absValue, value = heapq.heappop(heap)
#         result.append(value)
#     else:
#         heapq.heappush(heap, (abs(a), a))

# print(*result, sep="\n")