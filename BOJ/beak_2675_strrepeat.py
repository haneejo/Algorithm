# 백준 2675 문자열 반복
# 파이참이 이상한거야 뭐야...........

# T = int(input())
# for _ in range(T):
#     R, S = input().split() # 3 ABC  , 5 /HTP
#     # word_list = []
#
#     for i in S:
#         print(i * int(R))
#
#     # print(word_list)
#     print()

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')
    print()