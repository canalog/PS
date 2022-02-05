# https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    s = [i.split(",") for i in sorted(s[2:-2].split("},{"), key=len)]
    for i in s:
        answer.extend(set(i) - set(answer))
        
    answer = [int(i) for i in answer]
    return answer


def solution(s):
    answer = []
    s = Counter(re.findall('\d+', s)) # 숫자 부분만 뽑아내서 등장 횟수 찾기 : Counter({'2':4, '1':3, '3':2, '4':1})
    print(list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])))
    print(list(map(int, [k for k, v in s.most_common()])))
