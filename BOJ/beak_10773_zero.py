# 백준 10773 제로 (스택)


# 이건 내가 처음에 푼 방식인데 왜 안돼? stick이랑 비슷하게 푼건데..
K = int(input())
stack = []

for _ in range(K):
    stack.append(int(input()))

# print(stack)
sum_v = 0
for i in range(K):
    pick = stack.pop()
    if pick == 0:
        stack.pop()
    else:
        sum_v += pick
print(sum_v)


# 이거는 구글링 해보면서 나중에 푼 코드
K = int(input())
stack = []

for i in range(K):
    pick = int(input())

    if pick == 0:
        stack.pop()
    else:
        stack.append(pick)

print(sum(stack))