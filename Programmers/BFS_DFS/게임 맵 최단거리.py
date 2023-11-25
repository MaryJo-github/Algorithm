"""
author: mary
date: 23.11.04
title: 게임 맵 최단거리
"""

from collections import deque

def solution(maps):    
    N = len(maps)
    M = len(maps[0])
    
    will_visit = deque()
    count_array = [[0]*M for i in range(N)]
    
    will_visit.append((0, 0, 1))
    
    while will_visit:
        (x, y, cnt) = will_visit.popleft()

        if x == N-1 and y == M-1:
            return cnt
        
        if count_array[x][y] == 0:
            count_array[x][y] = cnt
            
            if x+1 < N and maps[x+1][y] == 1:
                will_visit.append((x+1, y, cnt+1))
            if y+1 < M and maps[x][y+1] == 1:
                will_visit.append((x, y+1, cnt+1))
            if x-1 >= 0 and maps[x-1][y] == 1 and count_array[x-1][y] == 0:
                will_visit.append((x-1, y, cnt+1))
            if y-1 >= 0 and maps[x][y-1] == 1 and count_array[x][y-1] == 0:
                will_visit.append((x, y-1, cnt+1))
    
    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))