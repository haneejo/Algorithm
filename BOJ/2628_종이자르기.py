width, height = map(int,input().split())
line_cnt = int(input())
arr = [[0] * width for _ in range(height)]
for _ in range(line_cnt):
    where, num = map(int,input().split())

    for i in range(width):
        for j in range(height):
            if where == 0:

                arr[i][j]
