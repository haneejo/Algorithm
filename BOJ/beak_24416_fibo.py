# 백준 24416 피보나치 수 1

N = int(input())
cnt1 = 0
cnt2 = 0

def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

def fibonacci(n):
    global cnt2
    f[1],f[2] = 1,1..............
    포기 ..

fib(N)
print(cnt1)
