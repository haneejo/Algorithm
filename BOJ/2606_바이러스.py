# 백준 2606 바이러스 DFS
# 하나하나 차근차근 해보자..

computer = int(input())
link = int(input())
visited = [0] * (computer+1)
graph = list([] for _ in range(computer+1))

for _ in range(link):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
print(visited)
cnt = 0
def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    # return True

dfs(1)
print(cnt)
print(visited)