"""
author: mary
date: 23.07.15
title: K번째 수
"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
input_array = list(map(int, input().split()))

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    arr1 = []
    arr2 = []
    for i in range(1, len(array)):
        if pivot > array[i]:
            arr1.append(array[i])
        else:
            arr2.append(array[i])
    return quick_sort(arr1) + [pivot] + quick_sort(arr2)

print(quick_sort(input_array)[K-1])
