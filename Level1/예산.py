# https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    d.sort()
    sum = 0
    for i, num in enumerate(d):
        sum += num
        if sum > budget:
            return i
    return len(d)
