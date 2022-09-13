# 백준 1260 DFS와 BFS
# 개념 잡는 문제니까 완벽하게 익히기
# BFS는 교수님이 알려주신 코드 그대로 쓰니까 됐다

def dfs(V):
    print(V, end=" ")
    visited[V] = 1
    for i in graph[V]:
        if visited[i] == 0:
            dfs(i)

def bfs(V):
    visited = [0] * (N + 1)
    q = []
    q.append(V)
    visited[V] = 1

    while q:
        V = q.pop(0)
        print(V,end=" ")
        for i in graph[V]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[i] + 1


N, M, V = map(int,input().split())
graph = list([] for _ in range(N + 1))
visited = [0] * (N + 1)
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(V)
print()
bfs(V)

