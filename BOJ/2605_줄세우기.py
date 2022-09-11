# 백준 2605 줄세우기
# 혼자서 못풀었음.. .insert()함수 배워가자

N = int(input())
num = list(map(int,input().split()))
arr = []

for i in range(len(num)):
    arr.insert(i-num[i],i+1)

for i in arr:
    print(i,end=" ")

# print(arr)


