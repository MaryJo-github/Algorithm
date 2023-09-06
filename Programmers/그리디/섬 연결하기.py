"""
author: mary
date: 23.09.07
title: 섬 연결하기
"""

# a = 4
# b = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

a = 5
b = [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]
### 정답은 7

def solution(n, costs):
    visit = [False] * n
    costs.sort(key=lambda x:x[2])

    sum = 0
    for cost in costs:
        if visit[cost[0]] and visit[cost[1]]:
            continue
        visit[cost[0]] = True
        visit[cost[1]] = True
        sum += cost[2]
    
    return sum

# def solution(n, costs):
#     answer = 0
#     costs.sort(key = lambda x: x[2]) 
#     link = set([costs[0][0]])

#     # Kruskal 알고리즘으로 최소 비용 구하기
#     while len(link) != n:
#         for v in costs:
#             if v[0] in link and v[1] in link:
#                 continue
#             if v[0] in link or v[1] in link:
#                 link.update([v[0], v[1]])
#                 answer += v[2]
#                 break
                
#     return answer

# def solution(n, costs):

#     def find_parent(parent, n):
#         if parent[n] != n:
#             parent[n] = find_parent(parent, parent[n])
#         return parent[n]
    
#     def union_parent(parent, a, b):
#         a = find_parent(parent, a)
#         b = find_parent(parent, b)
#         if a > b:
#             parent[a] = b
#         else:
#             parent[b] = a
    
#     answer = 0 
#     costs.sort(key=lambda x:x[2])  # 비용 기준으로 오름차순 정렬
#     parent = [i for i in range(n)]

#     for node_a, node_b, cost in costs:
#         if find_parent(parent, node_a) != find_parent(parent, node_b):
#             union_parent(parent, node_a, node_b)
#             answer += cost

#     return answer


print(solution(a, b))