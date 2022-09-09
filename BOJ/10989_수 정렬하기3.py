# 시간초과 코드
# N = int(input())
# num_list = []
#
# for _ in range(N):
#     num_list.append(int(input()))
#
#     num_list.sort()
#
# for i in num_list:
#     print(i)


# 어렵다... 메모리초과 시간초과도 생각해야하고 그냥 난 아직 for문에 대한 개념이 안 잡힌 것 같다.
import sys

N = int(input())
arr = [0] * 10001
for i in range(N):
    number = int(sys.stdin.readline())
    arr[number] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)