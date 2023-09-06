"""
author: mary
date: 23.09.05
title: 타겟 넘버
"""

import sys
input = sys.stdin.readline

# numbers = list(map(int, input().split()))
# target = int(input())
numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target):
    graph = [[] for _ in range(len(numbers)*2)]
    for i in range(len(numbers)-1):
        graph[i*2].append(((i+1)*2, numbers[i+1]))
        graph[i*2].append(((i+1)*2+1, -numbers[i+1]))
        graph[i*2+1].append(((i+1)*2, numbers[i+1]))
        graph[i*2+1].append(((i+1)*2+1, -numbers[i+1]))
    
    result = 0

    will_visit = []
    sum_array = [numbers[0]]
    will_visit.extend(graph[0])
    while will_visit:
        node = will_visit.pop()
        depth = node[0] // 2
        sum_array = sum_array[:depth]
        if graph[node[0]]:
            will_visit.extend(graph[node[0]])
            sum_array.append(node[1])
        else:
            sum_array.append(node[1])
            if sum(sum_array) == target:
                result += 1
                print(*sum_array)

    will_visit = []
    sum_array = [-numbers[0]]
    will_visit.extend(graph[1])
    while will_visit:
        node = will_visit.pop()
        depth = node[0] // 2
        sum_array = sum_array[:depth]
        if graph[node[0]]:
            will_visit.extend(graph[node[0]])
            sum_array.append(node[1])
        else:
            sum_array.append(node[1])
            if sum(sum_array) == target:
                result += 1

    return result


print(solution(numbers, target))