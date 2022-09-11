# 백준 2635 수이어가기
# 개뿌듯하다...........

num = int(input())
max_list = []

for i in range(1,num+1):
    new_list = [num]
    new_list.append(i)
    n = 1
    while True:
        if new_list[n-1] - new_list[n] >= 0:
            new_list.append(new_list[n-1] - new_list[n])
            n += 1
        else:
            break

    if len(max_list) < len(new_list):
        max_list = new_list

print(len(max_list))
for i in max_list:
    print(i,end=" ")