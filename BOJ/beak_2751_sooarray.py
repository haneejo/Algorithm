# 백준 2751 수 정렬하기 ( 시간복잡도 )

import sys

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
for i in num_list:
    print(i)