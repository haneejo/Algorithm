S = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_list = [-1] * len(alpha)

for i in range(len(alpha)):
    for j in range(len(S)):
        if alpha[i] == S[j]:
            alpha_list[i] = j
            break

for i in alpha_list:
    print(i,end=" ")