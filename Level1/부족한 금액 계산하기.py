# https://programmers.co.kr/learn/courses/30/lessons/82612
def solution(price, money, count):
    ans = sum(range(1, count+1)) * price - money
    return ans if ans > 0 else 0
