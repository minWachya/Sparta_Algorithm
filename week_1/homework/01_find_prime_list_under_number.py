input = 29


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        i = 0
        while len(prime_list) > i and prime_list[i] * prime_list[i] <= n:
            if n % prime_list[i] == 0:
                break
            i += 1
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)