# https://programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = [i for i in sorted(arr) if i % divisor == 0]
    if len(answer) == 0: answer = [-1]
    return answer
