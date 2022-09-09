# 백준 10952
# 브론즈지만 좀 특이한 인풋받기

while True:
    A, B = map(int,input().split())
    if A == 0 and B == 0:
        break
    else:
        result = A + B

    print(result)