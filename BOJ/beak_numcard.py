# 백준 10815 숫자카드
# 시간초과 나와서 딕셔너리 이용..
# 혹은 이진탐색으로 풀라하는데 나는 몰..라..

# 시간초과코드
# import sys
# N = int(sys.stdin.readline())
# sang_card = list(map(int,input().split()))
# M = int(sys.stdin.readline())
# sample_card = list(map(int,input().split()))
#
# yes = [0] * M
#
# for i in range(M):
#     for j in range(N):
#         if sample_card[i] == sang_card[j]:
#             yes[i] += 1
#
# for i in yes:
#     print(i,end=" ")

import sys
N = int(sys.stdin.readline())
sang_card = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
sample_card = list(map(int, sys.stdin.readline().split()))

new_dict = {}
result = 0
for i in range(N):
    new_dict[sang_card[i]] = 0
print(new_dict)

for j in range(M):
    if sample_card[j] not in new_dict:
        result = 0
    else:
        result = 1

    print(result,end=" ")