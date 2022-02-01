# https://www.acmicpc.net/problem/1260
def dfs(start):
    dfs_visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not dfs_visited[i]:
            dfs(i)

from collections import deque
def bfs(start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, start = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1, n+1):
    graph[i].sort()

dfs_visited = [False] * (n + 1)
  
dfs(start)
print()
bfs(start)
