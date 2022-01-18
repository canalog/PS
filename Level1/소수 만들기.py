# https://programmers.co.kr/learn/courses/30/lessons/12977
from itertools import combinations

def solution(nums):
    answer = 0
    
    comb = list(combinations(nums, 3))
    for c in comb:
        if is_prime(sum(c)):
            answer += 1

    return answer

def is_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
