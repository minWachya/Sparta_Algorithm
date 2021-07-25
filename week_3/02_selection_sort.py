input = [4, 6, 2, 9, 1]

# 선택 정렬
# [4, 6, 2, 9, 1]
# 제일 작은 거 찾아서 앞으로 옮기기
# [1, 6, 2, 9, 4]

# 맨 앞자리 제외 제일 작은 거 찾아서 앞으로 옮기기
# [1, 2, 6, 9, 4]

# 맨 앞자리 제외 제일 작은 거 찾아서 앞으로 옮기기
# [1, 2, 4, 9, 6]

# 맨 앞자리 제외 제일 작은 거 찾아서 앞으로 옮기기
# [1, 2, 4, 6, 9]


# 선택 정렬
# 선택해서 정렬하기
# O(N재곱)
def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[min_index] > array[i + j]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return array



selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!