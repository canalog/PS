# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = 0
    dartResult = dartResult.replace("10", "A") # A: 10점
    prev_score = 0
    curr_score = 0
    for i in dartResult:
        if i in "SDT":
            curr_score = curr_score ** ("SDT".index(i)+1)
        elif i == "*":
            curr_score *= 2
            answer += prev_score
        elif i == "#":
            curr_score *= -1
        else:
            prev_score = curr_score
            answer += prev_score
            if i == "A":
                curr_score = 10
            else:
                curr_score = int(i)
    answer += curr_score
    return answer
