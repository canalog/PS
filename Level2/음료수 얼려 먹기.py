# https://youtu.be/7C9RgOcvkvo?t=2689
def solution(s):
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        if graph[x][y] == 0:
            graph[x][y] = 1 # 해당 노드 방문 처리
            # 상하좌우의 위치도 모두 재귀적으로 호출
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        return False
    n = s[0]
    m = s[1]
    graph = s[2]
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    return result
    
print(solution([4, 5, [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]]))
