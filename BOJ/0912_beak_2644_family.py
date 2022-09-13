def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            arr[i] = arr[v] + 1
            dfs(i)

N = int(input())
A, B=map(int,input().split())
M = int(input())

graph=[[] for _ in range(N+1)]
visited = [0] * (N + 1)
arr=[0] * (N + 1)


for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(A)

if arr[B] > 0:
    print(arr[B])
else:
    print(-1)