"""
author: mary
date: 23.06.29
title: 트리의 지름
"""

import sys
from collections import deque
input = sys.stdin.readline

V = int(input())
graph = [[] for v in range(V+1)]

for _ in range(V):
    input_list = list(map(int, input().split()))
    for i in range(int(len(input_list)/2)-1):
        graph[input_list[0]].append((input_list[2*i+1],input_list[2*(i+1)]))
    graph[input_list[0]].sort(key=lambda x:x[1])

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (V+1)
    visited[start] = True
    res = [0, 0] # start로부터 가장 먼 거리에 있는 노드와 거리 값

    while q:
        cnt_node, cnt_dist = q.popleft()

        for adj_node, adj_dist in graph[cnt_node]:
            if not visited[adj_node]:
                cal_dist = cnt_dist + adj_dist
                q.append((adj_node, cal_dist))
                visited[adj_node] = True
                if res[1] < cal_dist:
                    res[0] = adj_node
                    res[1] = cal_dist
    
    return res

point, _ = bfs(1)
print(bfs(point)[1])

