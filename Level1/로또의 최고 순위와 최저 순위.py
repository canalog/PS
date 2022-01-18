# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    intersection_count = len(list(set(lottos).intersection(win_nums)))
    num_of_unknown = lottos.count(0)
    max_same = rank[intersection_count + num_of_unknown]
    min_same = rank[intersection_count]
    answer = [max_same, min_same]
    return answer
