# 백준 7568번 덩치
# 브루트포스.. 어렵다

N = int(input())
XY_list = []

for i in range(N):
    X, Y = map(int,input().split())
    XY_list.append((X,Y))

for i in XY_list:
    rank = 1
    for j in XY_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank)

# 5
# 55 185
# 58 183
# 88 186
# 60 175
# 46 155

