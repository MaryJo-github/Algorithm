"""
author: mary
date: 23.06.16
title: 수들의 합 5
"""

N = int(input())

head = -1
cnt = 0
while head < N:
    head += 1
    tail = head
    sum = 0
    while tail < N and sum <= N:
        # print(head, tail, sum)
        sum += tail
        if sum == N:
            cnt += 1
        tail += 1
print(cnt)

###### 경민
# N = int(input())

# start = 1
# end = 1
# count = 1
# sum = 1

# while start < N :
#     print(sum)
#     if sum == N:
#         count += 1
#         end += 1
#         sum += end
#     elif sum < N:
#         end += 1
#         sum += end
#     else :
#         sum -= start
#         start += 1

# print(count)
