# 5176. [기본] 8일차 - 이진탐색 (제출용)

def inorder(n):
    global cnt
    if n <= N:
        inorder(2 * n)
        tree[n] += cnt
        cnt += 1
        inorder(2 * n + 1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    inorder(1)

    print(f'#{tc}' ,tree[1],tree[N//2])
    # print(tree)
