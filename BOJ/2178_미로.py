N,M = map(int,input().split())
miro = list(input() for _ in range(N))

visited = [[0] * M for _ in range(N)]
dx , dy = [-1,1,0 ,0], [0,0,-1,1]
q =[(0,0)]
visited[0][0] = 1

while q:
    x,y = q.pop(0)
    if x == M-1 and y == N -1 :
        print(visited[y][x])
        break
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx < M and 0 <= ny < N:
                if miro[ny][nx] == '1' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] +1
                    q.append((nx,ny))