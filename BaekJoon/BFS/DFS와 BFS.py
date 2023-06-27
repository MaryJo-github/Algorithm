"""
author: mary
date: 23.06.27
title: DFS와 BFS
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
visited_list = []
def dfs(start):
    need_visit = deque()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if not visited[node]:
            visited[node] = True
            visited_list.append(node)
            need_visit.extend(sorted(graph[node], reverse=True))
dfs(V)
print(*visited_list)

visited = [False] * (N+1)
visited_list = []
def bfs(start):
    need_visit = deque([start])
    while need_visit:
        node = need_visit.popleft()
        if not visited[node]:
            visited[node] = True
            visited_list.append(node)
            need_visit.extend(sorted(graph[node]))

bfs(V)
print(*visited_list)
