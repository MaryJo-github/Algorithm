"""
author: mary
date: 23.07.11
title: 잃어버린 괄호
"""
import sys
input = sys.stdin.readline
formula = input().rstrip()
array = []
temp = ""
for str in formula:
    if str == "-" or str == "+":
        array.append(temp)
        array.append(str)
        temp = ""
        continue
    temp += str
array.append(temp)
print(array)

result = 0
temp = 0
flag = -1
for index, element in enumerate(array):
    if element == '-':
        flag = 1
        result -= temp
        temp = 0
        continue
    elif element == '+':
        continue
    if flag == 1:
        temp += int(element)
        if index == len(array)-1:
            result -= temp
    else:
        result += int(element)
print(result)

    
    