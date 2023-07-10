"""
author: mary
date: 23.07.10
title: 회의실 배정
"""
import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    start, end = list(map(int, input().split()))
    array.append((start, end))
array.sort(key = lambda x: (x[0], x[1]))

for n in range(N):
    start, end = array[n]
    