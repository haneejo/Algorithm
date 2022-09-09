# 백준 25340 영수증
# 브론즈5고 쉬운건데 어렵게 생각해서 생각보다 오래걸림
# 기본기 좀 제대로 다지자..

all_price = int(input())
N = int(input())
real_price = 0
for i in range(N):
    a,b = map(int,input().split())
    real_price += a * b

if real_price == all_price:
    print("Yes")
else:
    print("No")