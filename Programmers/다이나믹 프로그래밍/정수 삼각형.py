"""
author: mary
date: 23.09.06
title: 정수 삼각형
"""

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    for i in range(1, len(triangle)+1):
        arr = triangle[-i]
        for j in range(len(arr)-1):
            triangle[-i-1][j] += max(arr[j], arr[j+1])
    
    return triangle[0][0]

print(solution(triangle))