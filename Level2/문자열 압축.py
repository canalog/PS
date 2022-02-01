# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 길이 1일 때 for문에 들어가지 않는 경우 처리!
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        cnt = 0
        temp = ""
        prev = ""
        split_s = [s[j:j+i] for j in range(0, len(s), i)]
        split_s.append("")
        for j in split_s:
            if j != prev:
                if cnt > 1:
                    temp += str(cnt)
                temp += prev
                cnt = 0
            prev = j
            cnt += 1
        if answer == 1 or len(temp) < answer:
            answer = len(temp)
    return answer
