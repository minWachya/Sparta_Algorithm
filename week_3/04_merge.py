array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]

# 병합 정렬
def merge(array1, array2):
    result = []

    index_1 = 0
    index_2 = 0

    while index_1 < len(array1) and index_2 < len(array2):
        if array1[index_1] < array2[index_2]:
            result.append(array1[index_1])
            index_1 += 1
        else:
            result.append(array2[index_2])
            index_2 += 1

    if index_1 == len(array1):
        while index_2 < len(array2):
            result.append(array2[index_2])
            index_2 += 1

    if index_2 == len(array2):
        while index_1 < len(array1):
            result.append(array1[index_1])
            index_1 += 1

    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!