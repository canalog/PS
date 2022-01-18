# https://programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    wh = (*list(zip(*sizes)),)
    return max(wh[0]) * max(wh[1])

'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
'''
