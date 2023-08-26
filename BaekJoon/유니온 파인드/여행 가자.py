"""
author: mary
date: 23.08.18
title: 여행 가자
"""

import sys
input = sys.stdin.readline       

N = int(input())
M = int(input())
array = [i for i in range(N+1)]

def find_parent(node):
    while array[node] != node:
        node = array[node]
    return node

for n in range(N):
    temp = list(map(int, input().split()))
    n_parent = find_parent(n+1)
    for k in range(n+1, N):
        if temp[k] == 1:
            array[find_parent(k+1)] = n_parent

flag = True
plans = list(map(int, input().split()))
for m in range(0, M-1):
    if find_parent(plans[m]) != find_parent(plans[m+1]):
        flag = False

if flag:
    print("YES")
else:
    print("NO")

