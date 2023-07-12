"""
author: mary
date: 23.07.12
title: 소트인사이드
"""
import sys
input = sys.stdin.readline
N = input().rstrip()
array = [int(char) for char in N]

for k in range(len(array)-1):
    max = [-1, -1]
    for n in range(k, len(array)):
        if max[0] < array[n]:
            max[0] = array[n]
            max[1] = n

    array[max[1]] = array[k]
    array[k] = max[0]

print(*array, sep="")