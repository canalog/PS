# https://programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = []
    for i in s:
        if i == " ": answer.append(" ")
        else:
            new_i = ord(i) + n
            if (new_i > 90 and ord(i) <= 90) or (new_i > 122 and ord(i) >= 97):
                new_i -= 26
            answer.append(chr(new_i))
    return "".join(answer)
