"""
author: mary
date: 23.06.18
title: DNA비밀번호
"""

S, P = map(int, input().split())
dnaArray = input()
a_min, c_min, g_min, t_min = map(int, input().split())
a, c, g, t = 0, 0, 0, 0
cnt = 0

# 첫 번째 윈도우
for p in range(P):
    if dnaArray[p] == "A":
        a += 1
    elif dnaArray[p] == "C":
        c += 1
    elif dnaArray[p] == "G":
        g += 1
    else:
        t += 1

if a >= a_min and c >= c_min and g >= g_min and t >= t_min:
    cnt += 1

# 이후 윈도우
for s in range(1, S-P+1):
    if dnaArray[s-1] == "A":
        a -= 1
    elif dnaArray[s-1] == "C":
        c -= 1
    elif dnaArray[s-1] == "G":
        g -= 1
    else:
        t -= 1
    
    if dnaArray[s+P-1] == "A":
        a += 1
    elif dnaArray[s+P-1] == "C":
        c += 1
    elif dnaArray[s+P-1] == "G":
        g += 1
    else:
        t += 1
    
    if a >= a_min and c >= c_min and g >= g_min and t >= t_min:
        cnt += 1

print(cnt)