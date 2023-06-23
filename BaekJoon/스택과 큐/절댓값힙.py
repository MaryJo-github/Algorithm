"""
author: mary
date: 23.06.22
title: 절댓값힙
"""

# from collections import deque

# N = int(input())
# # array = [int(input()) for i in range(N)]
# result = []
# sortD = deque()

# for n in range(N):
#     a = int(input())
#     if a == 0:
#         if len(sortD) == 0:
#             result.append(0)
#             break
#         sign, value = sortD.popleft()
#         result.append(sign * value)
#     else:
#         sortD.append((, abs(a)))

import heapq

N = int(input())
heap = []
result = []

for n in range(N):
    a = int(input())
    if a == 0:
        if len(heap) == 0:
            result.append(0)
            continue
        absValue, value = heapq.heappop(heap)
        result.append(value)
    else:
        heapq.heappush(heap, (abs(a), a))

print(*result, sep="\n")