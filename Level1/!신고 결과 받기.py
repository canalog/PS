# https://programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {i: 0 for i in id_list} # 각 유저가 신고당한 횟수
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    return answer
