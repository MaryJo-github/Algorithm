"""
author: mary
date: 23.06.18
title: DNA비밀번호
"""

S, P = map(int, input().split())
dnaArray = input()
a_min, c_min, g_min, t_min = map(int, input().split())

window = P
for s in range(S):
    dnaArray_tmp = dnaArray[s:] + dnaArray[:s]
    password = dnaArray_tmp[0:0+window]
    print(password.count("A"))

