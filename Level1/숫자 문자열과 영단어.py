# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = 0
    num_in_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for num, eng in enumerate(num_in_eng):
        s = s.replace(eng, str(num))
    return int(s)
