"""
author: mary
date: 23.07.12
title: 수 정렬하기
"""
import sys
input = sys.stdin.readline
N = int(input())
array = [int(input()) for _ in range(N)]

for _ in range(N-1):
    for n in range(N-1):
        left = array[n]
        right = array[n+1]
        if left > right:
            array[n] = right
            array[n+1] = left
print(*array, sep="\n")