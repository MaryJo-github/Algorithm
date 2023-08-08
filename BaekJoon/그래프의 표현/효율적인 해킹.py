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
    
# def DFS(start):
#     count = 0
#     visited = [False] * (N+1)
#     visited[0] = True

#     visit_list = deque()
#     visit_list.extend(graph[start])
#     visited[start] = True

#     while visit_list:
#         node = visit_list.pop()        
#         if visited[node] == False:
#             visited[node] = True
#             count += 1
#             visit_list.extend(graph[node])
#     return count

# dfs_result = [-1]
# for n in range(1, N+1):
#     node, count = DFS(n)
#     dfs_result.append(dfs_result[node]+count)

# for n in range(N):
#     if dfs_result[n] == max(dfs_result):
#         print(n, end=" ")

global_visited = [False] * (N+1)
global_visited[0] = True 

dfs_result = [-1] * (N+1)
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
            if global_visited[node] == False:
                global_visited[node] = True
                
            if dfs_result[node] != -1:
                return count + dfs_result[node]
            else:
                dfs_result[node] = DFS(node)
                return count + dfs_result[node]
    return count

result = []
for n in range(1, N+1):
    if global_visited[n] == False:
        result.append(DFS(n))

for n in range(N):
    if dfs_result[n] == max(dfs_result):
        print(n, end=" ")