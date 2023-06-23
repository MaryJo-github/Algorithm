"""
author: mary
date: 23.06.22
title: 연결 요소의 개수
"""

N, M = map(int, input().split())
graph = {n+1: [] for n in range(N)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = list()
def dfs(graph, start_node):
    need_visited = list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    return visited

cnt = 0
for i in range(1, N+1):
    if i not in visited:
        dfs(graph, i)
        cnt += 1
print(cnt)
