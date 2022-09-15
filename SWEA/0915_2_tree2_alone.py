# 5178. 노드의 합 (제출용)

def postorder(n):
    if n <= N:
        postorder(2*n)
        postorder(2*n+1)
        if tree[n] == 0:
            if 2*n+1 > N:
                tree[n] = tree[2 * n]
                # return 0
            else:
                tree[n] = tree[2*n] + tree[2*n+1]

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        lst = list(map(int,input().split()))
        tree[int(lst[0])]  = int(lst[1])

    postorder(1)
    # print(tree)
    print(f'#{tc} {tree[L]}')
