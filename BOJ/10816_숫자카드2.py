# 백준 10816 숫자카드2
# 시간복잡도...

# 시간초과 코드
# import sys
# N = int(sys.stdin.readline())
# have = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# check = list(map(int, sys.stdin.readline().split()))
#
# new_dict = {}
# for i in range(M):
#     new_dict[check[i]] = 0
#     for j in range(N):
#         if check[i] == have[j]:
#             new_dict[check[i]] += 1
#
# for i in new_dict:
#     print(new_dict[i], end=" ")



import sys
N = int(sys.stdin.readline())
have = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

new_dict = {}
for i in have:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1

result = 0
for i in check:
    if i in new_dict:
        result = new_dict[i]
    else:
        result = 0
    print(result, end=" ")