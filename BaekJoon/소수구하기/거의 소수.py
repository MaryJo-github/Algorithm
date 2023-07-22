"""
author: mary
date: 23.07.22
title: 거의 소수
"""

import sys
input = sys.stdin.readline
A, B = list(map(int, input().split()))

max_num = int(B**0.5)+1
true_false_list = [True] * max_num
true_false_list[1] = False

for i in range(2, max_num):
    if true_false_list[i] == True:
        for j in range(2 * i, max_num, i):
            true_false_list[j] = False

count = 0
for element in range(2, max_num):
    if not true_false_list[element]:
        continue
    a = 2
    flag = True
    while flag:
        b = element**a
        if b <= B and b >= A:
            count += 1
            a += 1
        elif b > B:
            flag = False
        else:
            a += 1

print(count)