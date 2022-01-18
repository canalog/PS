# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    result = []
    while n:
        r = n % 3
        if r == 0:
            r = 3
            n -= 1
        result.append(str(r))
        n //= 3
    return "".join(result[::-1]).replace("3", "4")
