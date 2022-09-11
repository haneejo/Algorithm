# 백준 2491 수열
# 구글링해서 풀었음 나 존나못해 개못해 왜 안늘어?
# DP문제라는데 DP로 푸는 법도 알아보기

N = int(input())
num = list(map(int,input().split()))
# 1 2 2 4 4 5 7 7 2
# 4 1 3 3 2 2 9 2 3

cnt = 1
max_v = 1
for i in range(N-1):
    if num[i] <= num[i+1]:
        cnt += 1
    else:
        cnt = 1
    if max_v < cnt:
        max_v = cnt

cnt = 1
for i in range(N-1):
    if num[i] >= num[i+1]:
        cnt += 1
    else:
        cnt = 1
    if max_v < cnt:
        max_v = cnt

print(max_v)

