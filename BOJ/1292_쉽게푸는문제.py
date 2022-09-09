# 백준 1292 쉽게 푸는 문제

A, B = map(int,input().split())

new_list = []
for i in range(1,300):
    new_list.append(i)
    n = i
    while n > 1:
        n -= 1
        new_list.append(i)

sum_v = 0
for j in range(A,B+1):
    sum_v += new_list[j-1]

# print(new_list)
print(sum_v)