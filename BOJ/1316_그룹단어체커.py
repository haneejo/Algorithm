# 백준 1316 그룹단어 
# 어렵다 다시 한번 풀어보자
# 구현은 쉬운데 로직을 찾기가 힘들다

N = int(input())
result = N

for _ in range(N):
    word = input()

    for i in range(0,len(word)-1):
        if word[i] == word[i+1]:
            pass
        else:
            if word[i] in word[i+1:]:
                result -= 1
                break
print(result)