# bingo = [list(map(int,input().split())) for _ in range(5)]
# for _ in range(5):
#     call = list(map(int,input().split()))
#
#     for i in range(5):
#         for j in range(5):
#             if call[i][j] in bingo:


n = int(input())

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)