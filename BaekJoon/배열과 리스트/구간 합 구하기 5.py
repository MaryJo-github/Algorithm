"""
author: mary
date: 23.06.13
title: 구간 합 구하기 5
"""

N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

# 구간합
subSumRow = [[0] * N for _ in range(N)]
for n in range(N):
    sum = 0
    for n2 in range(N):
        sum += array[n][n2]
        subSumRow[n][n2] = sum

subSumColumn = [[0] * (N+1) for _ in range(N+1)]
for n2 in range(N):
    sum = 0
    for n in range(N):
        sum += subSumRow[n][n2]
        subSumColumn[n+1][n2+1] = sum

# result
resultList = [0] * M
for m in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = subSumColumn[x2][y2] - subSumColumn[x1-1][y2] - subSumColumn[x2][y1-1] + subSumColumn[x1-1][y1-1]
    resultList[m] = result

for m in range(M):
    print(resultList[m])


# 1234
# 2345
# 3456
# 4567

# 1 3 6 10
# 2 5 9 14
# 3 7 12 18
# 4 9 15 22

# 1 3 6 10
# 3 8 15 24
# 6 15 27 42
# 10 24 42 64