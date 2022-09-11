# 백준 13300 방배정
# 어렵다... 꼭 다시 보기

student, max_in = map(int,input().split())
girl = [0] * 7
boy = [0] * 7

for i in range(student):
    S, Y = map(int,input().split())
    if S == 0:
        girl[Y] += 1
    else:
        boy[Y] += 1

result = []
for i in range(1,7):
    if girl[i] % max_in == 0:
        result.append(girl[i] // max_in)
    else:
        result.append((girl[i] // max_in) + 1)

    if boy[i] % max_in == 0:
        result.append(boy[i] // max_in)
    else:
        result.append((boy[i] // max_in) + 1)

print(sum(result))
