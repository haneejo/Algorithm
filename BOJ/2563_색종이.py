# 백준 2563 색종이

N = int(input())
big_paper = [[0] * 100 for _ in range(100)]
for _ in range(N):
    width, height= map(int,input().split())
    # (width,height) (width+10, height+10)

    for i in range(width,width+10):
        for j in range(height,height+10):
            big_paper[i][j] = 1

result = 0
for i in big_paper:
    result += sum(i)
print(result)