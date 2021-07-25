finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 숫차 탐색
# O(logN)
# 연산량이 반으로 나눠진다 = O(logN)
def is_existing_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_max + cur_min) // 2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_max + cur_min) // 2
    return False

# 순차 탐색
# O(N)
def is_existing_target_number_sequential(target, array):
    find_count = 0
    for number in array:
        find_count += 1
        if target == number:
            print(find_count) # 14!
            return True

    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)