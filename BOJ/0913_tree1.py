def inorder(a):
    if a <= N:
        inorder(a * 2)
        print(tree[a],end=" ")
        inorder(a * 2 + 1)


for tc in range(1,11):
    N = int(input())
    graph = [0] * (N+1)

    for i in range(N):
        tree = list(input().split())
        graph[i + 1] = tree[1]
    print(f'#{tc}',end=" ")
    inorder(1)
    print()