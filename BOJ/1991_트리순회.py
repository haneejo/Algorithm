def preorder(n):
    if n != ".":
        print(n, end="")
        preorder(tree[n][0])  # tree[key][value], 왼쪽 자식 노드
        preorder(tree[n][1])

def inorder(n):
    if n != ".":
        inorder(tree[n][0])
        print(n, end="")
        inorder(tree[n][1])

def postorder(n):
    if n != ".":
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n, end="")


N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)


preorder("A")
print()
inorder("A")
print()
postorder("A")