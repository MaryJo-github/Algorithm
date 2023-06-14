"""
author: mary
date: 23.06.14
title: 2차원 배열의 합
"""

N, M = map(int, input().split())
array = []
for n in range(N):
    array.append(list(map(int, input().split())))

subSum = [[0] * M for _ in range(N)] 
for n in range(N):
    for m in range(M):
        if m == 0:
            subSum[n][m] = array[n][m]
        else:
            subSum[n][m] = subSum[n][m-1] + array[n][m]

subSum2 = [[0] * (M+1) for _ in range(N+1)]
for n in range(N):
    for m in range(M):
        if n == 0:
            subSum2[n+1][m+1] = subSum[n][m]
        else:
            subSum2[n+1][m+1] = subSum2[n][m+1] + subSum[n][m]

K = int(input())
resultList = []
for k in range(K):
    i, j, x, y = list(map(int, input().split()))
    result = subSum2[x][y] - subSum2[i-1][y] - subSum2[x][j-1] + subSum2[i-1][j-1]
    resultList.append(result)

for result in resultList:
    print(result)