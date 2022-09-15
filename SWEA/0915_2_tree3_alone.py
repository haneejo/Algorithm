# 5177. [기본] 8일차 - 이진 힙 (제출용)

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[c] < heap[p]:
        heap[c], heap[p] = heap[p], heap[c]
        c = p
        p = c//2

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num = list(map(int,input().split()))
    last = 0
    heap = [0] * (N+1)

    for i in num:
        enq(i)

    result = 0
    while heap[N] >0:
        result += heap[N//2]
        N = N // 2

    print(heap)
    print(result)