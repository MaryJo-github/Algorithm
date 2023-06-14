"""
author: mary
date: 23.06.13
title: 구간 합 구하기 4
"""

N, M = map(int, input().split())
data = list(map(int, input().split()))

sumList = []
beforeValue = 0
for i in data:
    sumList.append(beforeValue+int(i))
    beforeValue += i

resultList = []
for i in range(M):
    k, j = map(int, input().split())
    if k < 2:
        resultList.append(sumList[j-1])
    else:
        resultList.append(sumList[j-1]-sumList[k-2])

for i in range(M):
    print(resultList[i])

