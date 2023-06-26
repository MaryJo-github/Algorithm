"""
author: mary
date: 23.06.26
title: ABCDE
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    visited[start] = True
    if depth == 5:
        print(1)
        exit()
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[start] = False

for i in range(N):
    dfs(i, 1)

print(0)

# 1, 2, 3, 0
# 4, 1, 2, 3, 0

# 0: [1,3]
# 1: [0,2,4]
# 2: [1,3]
# 3: [0,2]
# 4: [1]

