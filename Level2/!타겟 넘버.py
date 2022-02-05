# https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    def dfs(index, result):
        if index == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(index + 1, result + numbers[index])
            dfs(index + 1, result - numbers[index])
    return answer
