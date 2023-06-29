"""
author: mary
date: 23.06.29
title: 트리의 지름
"""

from collections import deque
import sys
input = sys.stdin.readline

V = int(input())
graph = {v+1:[] for v in range(V)}

for v in range(V):
    input_list = list(map(int, input().split()))
    for i in range(int(len(input_list)/2)-1):
        graph[input_list[0]].append((input_list[2*i+1],input_list[2*(i+1)]))
    graph[input_list[0]].sort(key=lambda x:x[1])


def bfs(start):
    visited = [False] * V
    queue = deque(graph[start][-1])
    visited[start] = True
    visited_dist = 

    while queue:
        (n, m) = queue.pop()
        if not visited[n]:
            queue.append(graph[n][-1])
            visited[n] = True
            visited_dist += m

