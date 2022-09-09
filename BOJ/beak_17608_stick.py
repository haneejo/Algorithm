# 백준 17608 막대기 (스택)

# 스택 문제인데 스택 말고 그냥 리스트로 품
# import sys
#
# N = int(sys.stdin.readline())
# stack = []
# for _ in range(N):
#     stack.append(int(sys.stdin.readline()))
#
# cnt = 1
# max_v = stack[-1]
# for i in range(N-1,-1,-1):
#     if stack[i] > max_v:
#         max_v = stack[i]
#         cnt += 1
#
# print(cnt)



# 스택으로 풀어보자

import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    stack.append(int(sys.stdin.readline()))

max_v = 0
cnt = 0
for i in range(N):
    pick = stack.pop()
    if pick > max_v:
        max_v = pick
        cnt += 1
print(cnt)