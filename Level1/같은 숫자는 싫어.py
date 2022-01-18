# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if i != answer[-1]:
            answer.append(i)
    return answer
