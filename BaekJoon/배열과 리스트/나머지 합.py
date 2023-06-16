"""
author: mary
date: 23.06.15
title: 나머지 합
"""

N, M = list(map(int, input().split()))
array = list(map(int, input().split()))

# 구간합
subSum = [0] * N
sum = 0
for n in range(N):
    sum += array[n]
    subSum[n] = sum

# 구간합 중 M으로 나눴을 때 나머지가 0인 것
remain = [x for x in subSum if x % M == 0]
result = len(remain[x])
print(result)

# 나머지가 x인 개수 중 2개 선택
for m in range(M):
    if 