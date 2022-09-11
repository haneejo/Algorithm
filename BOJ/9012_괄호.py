# 백준 9012 괄호
# swea에서 스택 대표문제로 풀었던건데 혼자 다시 풀어보니까 또 막혔음
# 스웨아꺼랑 같이해서 다시 한번 보기

T = int(input())
for _ in range(T):
    test = input()
    stack = []
    result = 0

    for i in range(len(test)):
        if test[i] == '(':
            stack.append('(')
        elif test[i] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                result = "NO"
                break

        if len(stack) == 0:
            result = "YES"
        else:
            result = "NO"

    print(result)
