# https://programmers.co.kr/learn/courses/30/lessons/62048
# w와 h의 최대 공약수가 있을 때, w, h를 이로 나눈 w', h' (서로소)로 축소
# w'-1, h'-1 각각의 가로, 세로선을 지날 때마다 새로운 정사각형 추가
# 첫 정사각형 포함 1 + (w'-1) + (h'-1) = w' + h' - 1개의 정사각형 지남
# 최대공약수로 다시 곱해주면 전체 대각선은 w + h - gcd(w, h)개의 정사각형 지남
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(w,h):
    return w * h - (w + h - gcd(w, h))
