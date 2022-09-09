# 백준 1157 단어 공부

# word = input().upper()
#
# max_len = []
# result = 0
# for i in range(len(word)-1):
#     cnt_list = [word[i]]
#     for j in range(i+1,len(word)):
#         if word[i] == word[j]:
#             cnt_list.append(word[i])
#             if len(cnt_list) >= len(max_len):
#                 result = cnt_list[0]
#                 word.strip(word[i])
#             if len(cnt_list) == len(max_len):
#                 result = "?"
#
# print(result)
# print(word)



# word = input().upper()
# word_set = list(set(word))
#
# cnt = []
# for i in word_set:
#     cnt.append(word.count(i))
#
# if cnt.count(max(cnt)) > 1:
#     print("?")
# else:
#     print(word_set[cnt.index(max(cnt))])

# print(word_set)
# print(cnt)


word = input().upper()
word_set = list(set(word))

cnt_list = []
for i in word_set:
    cnt = 0
    for j in word:
        if i == j:
            cnt += 1
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(word_set[cnt_list.index(max(cnt_list))])