"""
author: mary
date: 23.08.10
title: 이분 그래프
"""

from collections import deque
import sys
input = sys.stdin.readline

def is_이분그래프(v, e):
    visited = [False] * (v+1)
    is_black = [False] * (v+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append([b, a])
        graph[b].append([a, b])
    
    for k in range(1, V+1):
        if not visited[k]:
            visit_list = deque()
            visit_list.extend(graph[k])
            visited[k] = True
            is_black[k] = True
            while visit_list:
                [node, before_node] = visit_list.popleft()
                if visited[node] == False:
                    visited[node] = True
                    is_black[node] = not is_black[before_node]
                    visit_list.extend(graph[node])
                else:
                    if is_black[node] == is_black[before_node]:
                        return False
    return True

results = []
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    results.append(is_이분그래프(V, E))

for result in results:
    if result:
        print("YES")
    else:
        print("NO") 