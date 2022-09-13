# 백준 16173 점프왕젤리
# DFS BFS 문제
# 구글 보고 풀었으니까 다시 풀어보기

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]  # 게임판 구역
visited = [[0] * N for _ in range(N)]   # 방문 여부 저장할 리스트

def dfs(x,y):
    # 영역을 벗어났거나 이미 방문 했다면
    if x <= -1 or x >= N or y <= -1 or y >= N or visited[x][y] == 1:
        return

    # 방문한 곳의 이동 칸수가 -1 이라면 방문처리
    if graph[x][y] == -1:
        visited[x][y] = 1
        return

    # 방문 표시
    visited[x][y] = 1

    # 상, 하 , 좌, 우를 요소 수만큼 점프하여 방문
    dfs(x + graph[x][y],y)
    dfs(x,y+graph[x][y])

dfs(0,0)    # 출발지점
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')