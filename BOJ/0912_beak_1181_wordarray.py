N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input().strip())

word_set = set()

word_list.sort()
word_list.sort(key = len)

for i in word_list:
    word_set.add(i)
word_list = list(word_set)
print(word_list)

for i in word_list:
    print(i)