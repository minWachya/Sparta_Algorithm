input = [4, 6, 2, 9, 1]

# 삽입 정렬
# [4, 6, 2, 9, 1]
# 1번째 원소 6 입장 및 비교
# 4 < 6 : 그대로 [4, 6, / 2, 9, 1] break

# 2번째 원소 2 입장 및 비교
# 6 > 2 : 교환 [4, 2, 6, / 9, 1]
# 4 > 2 : 교환 [2, 4, 6, / 9, 1]

# 3번째 원소 9 입장 및 비교
# 6 < 9 : 그대로 [2, 4, 6, 9, / 1] break

# 마지막 원소 1 입장 및 비교
# 9 > 1 : 교환 [2, 4, 6, 1, 9]
# 6 > 1 : 교환 [2, 4, 1, 6, 9]
# 4 > 1 : 교환 [2, 1, 4, 6, 9]
# 2 > 1 : 교환 [1, 2, 4, 6, 9]


# 삽입 정렬
# O(N제곱)
def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            # 버블 정렬과 선택 정렬엔 break없음
            # 비교 횟수 줄어듦
            else:
                break
    return array


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!