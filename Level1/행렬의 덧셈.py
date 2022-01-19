# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    return [list(map(sum,zip(*t))) for t in zip(arr1, arr2)]
