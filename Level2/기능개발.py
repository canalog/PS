# https://programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    days = []
    for i in range(0, len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    answer = [0]
    prev_d = days[0]
    for d in days:
        if d <= prev_d:
            answer.append(answer.pop()+1)
        else:
            prev_d = d
            answer.append(1)
    return answer
