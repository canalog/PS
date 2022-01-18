# https://programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter

def solution(participant, completion):
    answer = ''
    c1 = Counter(participant)
    c2 = Counter(completion)

    diff = c1 - c2
    return list(diff.elements())[0]
