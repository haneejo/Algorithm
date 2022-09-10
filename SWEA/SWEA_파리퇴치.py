T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    dx1 = [-1,1,1,-1]
    dx2 = [1,1,-1,-1]
    max_v = 0

    for i in range(N):
        for j in range(N):

            # +방향
            deadbug = arr[i][j]                     # 최댓값 찾기 전에 일단 가운데 인덱스 값 넣어놓기
            for k in range(1,M):                    # M 만큼 잡아야하기 때문에 범위 지정
                for l in range(4):                  # 곱할 델타인자(?) 수
                    ni = i + di[l] * k
                    nj = j + dj[l] * k
                    if 0<= ni < N and 0 <= nj < N:  # 범위 벗어나는 부분 제거
                        deadbug += arr[ni][nj]      # 구하고자하는 값 deaebug에 더해주기
            if deadbug > max_v:                     # 비교해서 최대값 저장
                max_v = deadbug

            # x 방향
            deadbug = arr[i][j]
            for k in range(1,M):
                for l in range(4):
                    nx1 = i + dx1[l] * k
                    nx2 = j + dx2[l] * k
                    if 0 <= nx1 < N and 0<= nx2 < N:
                        deadbug += arr[nx1][nx2]
            if deadbug > max_v:
                max_v = deadbug

    print(f'{tc} {max_v}')


