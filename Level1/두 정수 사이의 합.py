# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
    answer = sum(range(min(a,b), max(a,b)+1))
    # answer = (abs(a-b)+1)*(a+b) // 2 
    return answer
'''
