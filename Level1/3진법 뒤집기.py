# https://programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    answer = 0
    quo = n
    ternary = []
    while quo >= 3:
        quo, mod = divmod(quo, 3)
        ternary.append(mod)
    ternary.append(quo)
    ternary.reverse()
    for i, val in enumerate(ternary):
        answer += pow(3, i) * int(val)
    return answer
