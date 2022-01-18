# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    points = []
    times = int(len(answers) / 5 + 1)
    one = [1,2,3,4,5] * times
    two = [2, 1, 2, 3, 2, 4, 2, 5] * times
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * times
    for k in [one, two, three]:
        count = 0
        for i, j in zip(answers, k):
            if i == j:
                count += 1
        points.append(count)
    for i in range(len(points)):
        if points[i] == max(points):
            answer.append(i+1)
    return answer
