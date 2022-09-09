# 백준 4344번 평균은 넘겠지 (일차원 배열 )

C = int(input())
for tc in range(C):
    score = list(map(int,input().split()))

    student = score[0]

    sum_v = 0
    good = 0
    for i in range(1,len(score)):
        sum_v += score[i]
    aver = sum_v / student
    for i in range(1,len(score)):
        if score[i] > aver:
            good += 1
    result = (good / student) * 100
    print(f'{result:.3f}%')