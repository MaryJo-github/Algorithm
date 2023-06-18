"""
author: mary
date: 23.06.16
title: 주몽
"""

N = int(input())
M = int(input())
array = list(map(int, input().split()))

# first = 0
# second = 0
# cnt = 0
# while first < N-1:
#     while second < N:
#         if array[first] + array[second] == M:
#             cnt += 1
#             del array[first]
#             del array[second-1]
#             continue

cnt = 0
while len(array) > 2:
    choosen_idx = 0
    while choosen_idx < len(array):
        choosen_idx += 1
        if array[0] + array[choosen_idx] == M:
            cnt += 1
            array.pop(0)
            array.pop(choosen_idx-1)
            continue
            
print(cnt)