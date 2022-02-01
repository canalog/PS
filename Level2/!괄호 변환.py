# https://programmers.co.kr/learn/courses/30/lessons/60058
def solution(p):
    answer = ''
    if p == "": return p
    u, v = split_balanced(p)
    if is_right(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        answer += u[1:-1].replace(")", "a").replace("(", ")").replace("a", "(")

    return answer

def is_balanced(p):
    return p.count("(") == p.count(")")

def split_balanced(p):
    for i in range(2, len(p)+1, 2):
        if is_balanced(p[:i]): # 균형잡힌 괄호 문자열은 애초에 짝수 길이. 앞 문자만 균형잡히면 뒷 문자도 균형
            return (p[:i], p[i:])

def is_right(p):
    check = []
    for i in p:
        if i == "(":
            check.append("(")
        else:
            if not check:
                return False
            if check.pop() != "(":
                return False
    return len(check) == 0

'''
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
'''
