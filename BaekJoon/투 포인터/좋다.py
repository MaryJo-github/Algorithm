"""
author: mary
date: 23.06.18
title: 좋다
"""

N = int(input())
array = list(map(int, input().split()))
array.sort()

cnt = 0
for n in range(2, N): 
    first = 0
    second = n-1
    while second > first:
        target = array[n]
        compare = array[first]+array[second]
        if target == compare:
            cnt += 1
            break
        elif target > compare:
            first += 1
        elif target < compare:
            second -= 1

print(cnt)

# 문제: 3 5 8 9 11 12 14
# 답: 4 (8, 11, 12, 14)

# 문제: 3 3 6 8 8 9 11 12 14
# 답: 5 (6, 9, 11, 12, 14)

# 문제: 1 1 1 2 2 4 5 6 7 7
# 답: 7 (2, 2, 4, 5, 6, 7, 7)

# 문제: -5 -3 -1 1 3 4 6 7
# 답: ? ()


