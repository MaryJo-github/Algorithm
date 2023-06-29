"""
author: mary
date: 23.06.27
title: 미로탐색
"""

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for n in range(N):
    sub_arr = list(map(int, str(input().strip())))
    # sub_arr = [list(map(int, input())) for _ in range(N)]
    graph.append(sub_arr)

def bfs(si, sj, ei, ej):
    q = []
    v = [[0]*M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if (ci,cj) == (ei,ej):
            return v[ei][ej]

        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and graph[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj]+1

ans = bfs(0, 0, N-1, M-1)
print(ans)


# BFS(Breadth-First Search)는 그래프나 트리에서 최단 경로를 찾는 데 사용되는 탐색 알고리즘입니다. BFS를 사용하여 미로를 탐색할 때 최단 경로가 나오는 이유는 다음과 같습니다:

# 가까운 노드부터 탐색: BFS는 시작 노드에서부터 탐색을 시작하며, 현재 노드와 인접한 모든 노드를 탐색합니다. 이 때, 가장 가까운 노드부터 방문하게 되므로 최단 경로를 찾는 데 적합합니다.

# 레벨별 탐색: BFS는 노드를 탐색하는 순서에 따라 레벨별로 탐색을 진행합니다. 즉, 시작 노드에서부터 거리가 1인 노드들을 먼저 탐색하고, 그 다음에는 거리가 2인 노드들을 탐색하게 됩니다. 이러한 순서로 탐색하면서 각 노드에 도달하는데 걸리는 최소 이동 횟수를 계산할 수 있습니다.

# 큐(Queue)의 활용: BFS는 큐를 사용하여 노드를 저장하고 탐색 순서를 유지합니다. 각 레벨에서 인접한 노드들을 큐에 추가하고, 큐의 선입선출(FIFO) 특성에 따라 가장 가까운 노드부터 처리됩니다. 이를 통해 최단 경로를 탐색할 수 있게 됩니다.

# 따라서, BFS 알고리즘은 가까운 노드부터 차례대로 탐색하고, 레벨별로 탐색 순서를 유지하여 최단 경로를 찾아갑니다. 이러한 특성으로 인해 BFS를 사용하면 미로에서 시작점에서 도착점까지의 최단 경로를 탐색할 수 있습니다.