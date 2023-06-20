"""
author: mary
date: 23.06.16
title: 주몽
"""

N = int(input())
M = int(input())
array = list(map(int, input().split()))
array.sort()

first = 0
second = N-1
cnt = 0

while first < second:
    compare = array[first]+array[second]
    if M == compare:
        cnt += 1
        first += 1
    elif M > compare:
        first += 1
    else:
        second -= 1

print(cnt)