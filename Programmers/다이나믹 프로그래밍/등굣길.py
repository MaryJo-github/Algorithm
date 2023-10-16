"""
author: mary
date: 23.10.16
title: 등굣길
"""

def solution(m, n, puddles):
    array = [[-1] * m for _ in range(n)]
    
    for puddle in puddles:
        if puddle[0] == 1:
            for i in range(puddle[1]-1, n):
                array[i][0] = 0  
        elif puddle[1] == 1:
            for i in range(puddle[0]-1, m):
                array[0][i] = 0
        else:
            array[puddle[1]-1][puddle[0]-1] = 0
    
    for b in range(n):
        for a in range(m):
            if array[b][a] == 0:
                continue
            if a == 0 or b == 0:
                array[b][a] = 1
                continue
            array[b][a] = array[b-1][a] + array[b][a-1]        
    
    return array[n-1][m-1] % 1000000007
