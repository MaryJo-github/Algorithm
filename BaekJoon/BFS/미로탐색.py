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