"""
author: mary
date: 23.08.13
title: 물통
"""

from collections import deque
import sys
input = sys.stdin.readline

def pour(x, y):
    if not visited_list[x][y]:
        visited_list[x][y] = True
        queue.append([x, y])

def bfs():
    while queue:
        [x, y] = queue.popleft()
        z = C - x - y
        if x == 0:
            result.append(z)
        
        # A -> B
        water = min(x, B-y)
        pour(x - water, y + water)
        # A -> C
        water = min(x, C-z)
        pour(x - water, y)
        # B -> A
        water = min(y, A-x)
        pour(x + water, y - water)
        # B -> C
        water = min(y, C-z)
        pour(x, y - water)
        # C -> A
        water = min(z, A-x)
        pour(x + water, y)
        # C -> B
        water = min(z, B-y)
        pour(x, y + water)

A, B, C = map(int, input().split())
visited_list = [[False] * (B+1) for _ in range(A+1)]

queue = deque()
queue.append([0, 0])
visited_list[0][0] = True

result = []
bfs()
print(*sorted(result), end=" ")
