# 백준 24479 DFS 조오오오온나 어렵다 뭔 개소리니

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, R = map(int,input().split())
graph = list([] for _ in range(N + 1))
visited = [0] * (N + 1)
V = 1

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(R):
    global V
    visited[R] = V
    graph[R].sort()
    for i in graph[R]:
        if visited[i] == 0:
            V += 1
            dfs(i)

dfs(R)
for i in range(1,N+1):
    print(visited[i])

print(graph)
