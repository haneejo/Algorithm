# 백준 11478 서로 다른 문자열

# 시간초과 코드
# word = input() # ababc
#
# word_list = []
# for i in range(len(word)+1):
#     for j in range(i,len(word)):
#         if word[i:j+1] not in word_list:
#             word_list.append(word[i:j+1])
#
# print(len(word_list))



word = input() # ababc

word_set = set()
for i in range(len(word)+1):
    for j in range(i,len(word)):
        word_set.add(word[i:j+1])

print(len(word_set))
