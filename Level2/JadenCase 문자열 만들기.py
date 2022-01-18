# https://programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    s = list(s.lower())
    for i in range(len(s)):
        if s[i-1] == " " or i == 0:
            try:
                s[i] = s[i].upper()
            except:
                pass
    return "".join(s)
