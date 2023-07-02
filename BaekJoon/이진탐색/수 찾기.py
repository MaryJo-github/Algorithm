"""
author: mary
date: 23.06.29
title: 수 찾기
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().split()))
M = int(input().rstrip())
search_numbers = list(map(int, input().split()))

numbers.sort()
for search_number in search_numbers:
    start = 0
    end = N-1
    flag = 0

    while start <= end:
        median = (start+end)//2
        median_value = numbers[median]
        if search_number < median_value:
            end = median-1
        elif search_number > median_value:
            start = median+1
        else:
            flag = 1
            break
    print(flag)