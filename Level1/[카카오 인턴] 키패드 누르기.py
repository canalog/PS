# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    l_pos = 10
    r_pos = 11
    dist = {2: [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4], 5: [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3], 8: [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2], 0: [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1]}
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            l_pos = n
        elif n in [3, 6, 9]:
            answer += "R"
            r_pos = n
        else:
            chosen = ""
            if dist[n][l_pos] < dist[n][r_pos]: 
                chosen="L"
                l_pos = n
            elif dist[n][l_pos] > dist[n][r_pos]: 
                chosen="R"
                r_pos = n
            else: 
                chosen = hand.upper()[0]
                if chosen == "L": l_pos = n
                else: r_pos = n

            answer += chosen
    return answer
