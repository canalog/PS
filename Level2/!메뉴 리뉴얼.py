# https://programmers.co.kr/learn/courses/30/lessons/72411
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for o in orders:
            temp += combinations(sorted(o), c)
        most_ordered = Counter(temp).most_common()
        answer += ["".join(k) for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return sorted(answer)


'''
from itertools import combinations, chain
from collections import Counter

def solution(orders, course):
    answer = []
    condition = {k: 0 for k in course}
    candidates = [list(combinations(sorted(i), j)) for i in orders for j in course]
    counter_can = Counter(list(chain(*candidates)))
    total = [(k, v) for k, v in counter_can.most_common() if v >= 2]
    for i in total:
        len_course = len(i[0])
        if len_course in course and condition[len_course] <= i[1]:
            answer.append("".join(i[0]))
            condition[len_course] = i[1]

    return sorted(answer)
'''
