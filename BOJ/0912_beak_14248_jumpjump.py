N = int(input())
stone = [0] + list(map(int,input().split()))
S = int(input())
cnt = 0
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

def dfs(v):
    global cnt
    visited[v] = 1
    cnt += 1
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

dfs(S)
print(cnt)