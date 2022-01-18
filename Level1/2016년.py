# https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yoil = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    total_days = sum(days[:a-1])+(b-1)
    answer = yoil[total_days%7]
    return answer
