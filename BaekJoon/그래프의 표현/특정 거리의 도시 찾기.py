"""
author: mary
date: 23.08.07
title: 특정 거리의 도시 찾기
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

visited = [False] * (N + 1)
visited[0] = True
visit_list = deque()

result = []
visited[X] = True
visit_list.extend(graph[X])
while visit_list:
    (node, count) = visit_list.popleft()
    if visited[node] == False:
        visited[node] = True
        if count == K:
            result.append(node)
            continue
        for n in range(len(graph[node])):
            visit_list.append((graph[node][n][0], count+1))

if result == []:
    print(-1)
else:
    print(*sorted(result), sep="\n")
        
    




