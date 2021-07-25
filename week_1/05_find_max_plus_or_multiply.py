input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multifly_sum = 0
    for number in array:
        if number <= 1 or multifly_sum <= 1:
            multifly_sum += number
        else:
            multifly_sum *= number

    return multifly_sum


result = find_max_plus_or_multiply(input)
print(result)