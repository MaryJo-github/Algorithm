"""
author: mary
date: 23.06.18
title: 좋다
"""

N = int(input())
array = list(map(int, input().split()))
array.sort()

# 3 5 8 9 11 12 14
print(list(range(2, 1)))

first = 0
second = 1
cnt = 0
for n in range(2, N): 
    while second < N:
        target = array[n]
        compare = array[first]+array[second]
        if target == compare:
            cnt += 1
            if first+1 == second:
                second += 1
            else:
                first += 1
            break
        elif target > compare:
            if first+1 == second:
                second += 1
            else:
                first += 1
        elif target < compare:
            # if first+1 == second:
            #     break
            # else:         
            break

print(cnt)
