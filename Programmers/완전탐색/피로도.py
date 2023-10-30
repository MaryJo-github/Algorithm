"""
author: mary
date: 23.10.27
title: 피로도
"""

max_cnt = 0

def solution(k, dungeons):
    global max_cnt
    for i in range(len(dungeons)):
        calculation(k, dungeons[i], dungeons[:i] + dungeons[i+1:], 0)
    
    return max_cnt

def calculation(k, current, array, cnt):
    global max_cnt
    
    if k >= current[0]:
        k -= current[1]
        cnt += 1
            
        for i in range(len(array)):
            calculation(k, array[i], array[:i] + array[i+1:], cnt)
    
    if max_cnt < cnt:
        max_cnt = cnt
    
    return