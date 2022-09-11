# 백준 2669 직사각형 네개의 합집합의 면적 구하기
# 좌표 설정 잘 봐주기
# 그것만 이해하면 구현은 개쉬운문제

arr = [list([0] * 100) for _ in range(100)]

for _ in range(4):
    lx, ly, rx, ry = map(int,input().split())

    for i in range(lx,rx):
        for j in range(ly,ry):
            arr[i][j] = 1
result = 0
for i in arr:
    result += sum(i)
print(result)