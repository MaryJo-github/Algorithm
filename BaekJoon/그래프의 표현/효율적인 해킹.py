"""
author: mary
date: 23.08.08
title: 효율적인 해킹
"""

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    
global_visited = [False] * (N+1)
global_visited[0] = True 

def DFS(start):
    count = 1
    visited = [False] * (N+1)
    visited[0] = True

    visit_list = deque()
    visit_list.extend(graph[start])
    visited[start] = True

    while visit_list:
        node = visit_list.pop()
        
        if visited[node] == False:
            visited[node] = True
            count += 1
            visit_list.extend(graph[node])
            global_visited[node] = True
    return count

result = []
for n in range(1, N+1):
    if global_visited[n] == False:
        result.append((n,DFS(n)))

for n in range(len(result)):
    print(result[n][0], end=" ")