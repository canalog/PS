# https://programmers.co.kr/learn/courses/30/lessons/72410
import re

def solution(new_id):
    answer = ''
    answer = re.sub("[^a-z0-9_.\-]+","", new_id.lower())
    answer = re.sub("\.\.+", ".", answer)
    answer = answer.strip(".")
    if answer == "":
        answer = "a"
    answer = answer[:15].rstrip(".")
    answer += answer[-1]*(3-len(answer))
    return answer
