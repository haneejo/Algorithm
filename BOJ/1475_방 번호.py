# 백준 1475 방번호
# 딕셔너리 풀이
# n = input()
# a = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}
# for i in range(len(n)):
#     if n[i] in ['6', '9']:
#         a['6'] += 1
#     else:
#         a[n[i]] += 1
# if a['6'] % 2 == 0:
#     a['6'] = a['6'] // 2
# else:
#     a['6'] = a['6'] // 2 + 1
# print(max(a.values()))





N =  list(map(int,input()))
pn = [0] * 10

for i in range(len(N)):
    if N[i] == 9:
        pn[6] += 1
    else:
        pn[N[i]] += 1

result = 0
if pn[6] == max(pn) and pn[0] < pn[6] and pn[1] < pn[6] and pn[2] < pn[6] and pn[3] < pn[6] and pn[4] < pn[6] and pn[5] < pn[6] and pn[7] < pn[6] and pn[8] < pn[6] and pn[9] < pn[6]: #샹
    if pn[6] % 2 == 0:
        result = pn[6] // 2
    else:
        result = pn[6] // 2 + 1
else:
    result = max(pn)

print(result)