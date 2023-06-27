"""
author: mary
date: 23.06.27
title: 미로탐색
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# graph = [[[] for _ in range(M)] for _ in range(N)]
graph = []
for n in range(N):
    sub_arr = list(map(int, str(input().strip())))
    graph.append(sub_arr)
print(graph)

for n in range(N):
    for m in range(M):
        if graph[n, m] == 1:
            