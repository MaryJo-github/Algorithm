"""
author: mary
date: 23.07.11
title: 수 묶기
"""
import sys
input = sys.stdin.readline
N = int(input())

array_positive = []
array_negative = []
for _ in range(N):
    value = int(input())
    if value > 0:
        array_positive.append(value)
    else:
        array_negative.append(value)
array_positive.sort()
array_negative.sort(reverse=True)

def mul(array):
    result = 0
    while array:
        a = array.pop()
        try:
            b = array.pop()
        except:
            result += a
            break
        mul = a * b
        sum = a + b
        if mul > sum:
            result += mul
        else:
            result += sum
            if a == 0 or b == 0:
                array.append(0)
    return result

print(mul(array_positive) + mul(array_negative))


