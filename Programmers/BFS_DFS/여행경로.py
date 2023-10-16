"""
author: mary
date: 23.09.22
title: 여행경로
"""

# def solution(tickets):
#     answer = []
#     graph = dict([])
#     for ticket in tickets:
#         if not ticket[0] in graph:
#             graph[ticket[0]] = []
#         if not ticket[1] in graph:
#             graph[ticket[1]] = []
#         graph[ticket[0]].append(ticket[1])
    
#     for element in graph:
#         graph[element].sort(reverse = True)
    
#     for element in graph:
#         result = dfs(element, graph, tickets)
#         if result != []:
#             answer = result
#     return answer

# def dfs(start_node, graph, tickets):
#     used = [False] * len(tickets)
#     will_visit = graph[start_node].copy()
#     start = start_node
#     path = [start_node]
#     while will_visit:
#         end = will_visit.pop()
#         try:
#             index = tickets.index([start, end])
#             if not used[index]:
#                 used[index] = True
#                 will_visit.extend(graph[end])
#                 path.append(end)
#                 start = end
#         except:
#             continue
#     if all(used):
#         return path
#     else: 
#         return []

from collections import defaultdict

def solution(tickets):
    answer = []
    adj = defaultdict(list)

    for ticket in tickets:
        adj[ticket[0]].append(ticket[1])

    for key in adj.keys():
        adj[key].sort(reverse=True)

    q = ['ICN']
    while q:
        tmp = q[-1]

        if not adj[tmp]:
            answer.append(q.pop())
        else:
            q.append(adj[tmp].pop())
    answer.reverse()
    return answer

tickets = [['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]
print(solution(tickets))

# https://deok2kim.tistory.com/118