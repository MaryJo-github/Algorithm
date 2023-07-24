"""
author: mary
date: 23.07.23
title: 소수&팰린드롬
"""
import sys
input = sys.stdin.readline
N = int(input())

def is_prime_number(number):
    if number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def is_palindrome(number):
    number = str(number)
    for i in range(int(len(number)/2)):
        if number[i] != number[-1-i]:
            return False
    return True

while True:
    if is_palindrome(N) and is_prime_number(N):
        print(N)
        break
    N += 1