"""
author: mary
date: 23.06.12
title: 평균 구하기
time: 15분
"""

n = input()
data = list(map(float,input().split()))
sum = 0
for i in data:
    sum += i/max(data)*100
print(sum/len(data))
