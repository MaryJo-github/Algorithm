"""
author: mary
date: 23.06.19
title: 최솟값 찾기
"""

########## 풀이 1
# N, L = map(int, input().split())
# D = list(map(int, input().split()))

# minimum = D[0]
# result = [minimum]
# for n in range(1, N):
#     # 나가는 숫자와 min 비교
#     if n-L >= 0:
#         if minimum == D[n-L]:
#             minimum = min(D[n-L+1:n+1])

#     # 들어오는 숫자와 min 비교
#     if minimum > D[n]:
#         minimum = D[n]

#     result.append(minimum)

# print(result)

########## 풀이 2
from collections import deque

N, L = map(int, input().split())
D = list(map(int, input().split()))
minQue = deque([])

for n in range(N):
    while minQue and minQue[-1][1] > D[n] :
        minQue.pop()
    minQue.append((n, D[n]))
    if minQue[0][0] == n-L:
        minQue.popleft()
    print(minQue[0][1], end = " ")
