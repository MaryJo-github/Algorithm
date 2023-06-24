"""
author: mary
date: 23.06.22
title: 연결 요소의 개수
"""

from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
graph = {n+1: [] for n in range(N)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [False]*(N+1)
def dfs(graph, start_node):
    need_visited = list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if not check[node]:
            check[node] = True
            need_visited.extend(graph[node])

cnt = 0
for i in range(1, N+1):
    if not check[i]:
        dfs(graph, i)
        cnt += 1
print(cnt)
