# 백준 10157 자리배정
# 포기

W, H = map(int,input().split())
num = int(input())
arr = [[0] * W for _ in range(H)]

for i in range(W):
    for j in range(H):
        if arr[i][j] !=