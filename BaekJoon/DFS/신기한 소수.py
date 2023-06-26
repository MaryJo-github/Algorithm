"""
author: mary
date: 23.06.23
title: 신기한 소수
"""
import sys
input = sys.stdin.readline
N = int(input())
odd = [1, 3, 5, 7, 9]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

array2 = [2, 3, 5, 7]
for _ in range(N-1):
    array = array2
    array2 = []
    for i in array:
        for o in odd:
            if is_prime(10*i+o):
                array2.append(10*i+o)

print(*array2, end="\n")
