# https://programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    # 알파벳으로만 구성된 문자열 다중집합 만들기
    str1 = [i[0]+i[1].lower() for i in list(zip(str1[0:], str1[1:])) if i[0].isalpha() and i[1].isalpha()]
    str2 = [i[0]+i[1] for i in list(zip(str2[0:], str2[1:])) if i[0].isalpha() and i[1].isalpha()]
    # 자카드 유사도 구하기
    if not len(str1) and not len(str2):
        return 65536
    cnt = 0 # 교집합 크기
    for i in set(str1):
        cnt += min(str1.count(i), str2.count(i))
    total = len(str1) + len(str2) - cnt
    return int(cnt / total * 65536)
