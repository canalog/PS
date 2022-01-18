# https://programmers.co.kr/learn/courses/30/lessons/70128
def solution(a, b):
    return sum([i*j for i, j in zip(a, b)])
