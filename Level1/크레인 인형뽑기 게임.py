# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        m = m - 1
        for b in range(len(board)):
            if board[b][m] != 0:
                if len(basket) != 0 and basket[-1] == board[b][m]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[b][m])
                board[b][m] = 0
                break

    return answer
