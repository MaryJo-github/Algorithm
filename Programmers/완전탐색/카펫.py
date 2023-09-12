"""
author: mary
date: 23.09.13
title: 카펫
"""

def solution(brown, yellow):
    for width in range(1, brown+yellow):
        for height in range (1, width+1):
            if width * height == brown + yellow:
                if width + height == ((brown + 4)//2):
                    return [width, height]
