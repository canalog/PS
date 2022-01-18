# https://programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer = -1
    answer = sum([i for i in range(10) if i not in numbers])
    return answer
