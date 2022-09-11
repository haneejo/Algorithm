#백준 2309번 일곱난쟁이 ( 브루트포스 알고리즘 )

new_list = []                           # 아홉명의 난쟁이 키 값을 담아줄 리스트 생성
for i in range(9):                      # 아홉명의 난쟁이 키
    new_list.append(int(input()))       # 리스트에 세로로 하나씩 입력받기

for i in range(8):                      # 가짜 난쟁이 두 명 찾기 위한 범위 설정 (첫 번째 난쟁이)
    for j in range(i+1,len(new_list)):  # 두 번째 난쟁이 범위 설정
        if new_list[i] + new_list[j] == sum(new_list) - 100:    # 두 난쟁이를 더한 값이 아홉난쟁이의 합 -100의 값과 같은지
            a = new_list[i]
            b = new_list[j]
            new_list.remove(a)          # .remove()는 리스트 안의 특정 값 제거,
            new_list.remove(b)          # .pop()은 리스트 안의 특정값으 인덱스로 제거
            break

new_list.sort()
for i in new_list:
    print(i)                            # 제시된 출력 형식으로 나오게 하기 위해