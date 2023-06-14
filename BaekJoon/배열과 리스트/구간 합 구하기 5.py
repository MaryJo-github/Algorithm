"""
author: mary
date: 23.06.13
title: 구간 합 구하기 5
"""

N, M = map(int, input().split())
array = []
for i in range(N):
    array.append(list(map(int, input().split())))

resultList = [0] * M
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2+1):
        for k in range(y1, y2+1):
            resultList[i] += array[j-1][k-1]

for i in range(M):
    print(resultList[i])


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