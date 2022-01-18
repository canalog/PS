# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    answer = []
    fail_rate = []
    for stage in range(1, N+1):
        failed_count = stages.count(stage)
        reached_count = len(list(filter(lambda x: x >= stage, stages)))
        rate = 0 if reached_count == 0 else failed_count/reached_count
        fail_rate.append(rate)
    # 실패율이 높은 순으로 stage 저장
    answer = list(map(lambda x: x+1, sorted(range(len(fail_rate)), key=lambda x: fail_rate[x], reverse=True)))
    return answer
