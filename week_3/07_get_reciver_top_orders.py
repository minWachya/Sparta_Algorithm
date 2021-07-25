top_heights = [6, 9, 5, 7, 4]

# <- <- <- <- <-
# 6  9  5  7  4
# 7 > 4, 7은 4번째 탑
# [0, 0, 0, 0, 4]

# <- <- <- <-
# 6  9  5  7
# 9 > 7, 9은 2번째 탑
# [0, 0, 0, 2, 4]

# <- <- <-
# 6  9  5
# 9 > 5, 9은 2번째 탑
# [0, 0, 2, 2, 4]

# <- <-
# 6  9
# [0, 0, 2, 2, 4]

# <-
# 6
# [0, 0, 2, 2, 4]

# [6, 9, 5, 7, 4]가 끝에서부터 하나씩 사라짐 =>  스택 이용

# O(N제곱)
def get_receiver_top_orders(heights):
    result = [0] * len(heights)

    while heights:
        height = heights.pop()

        for index in range(len(heights) - 1, 0, -1):
            if heights[index] > height:
                # 스택에서 하나를 ㄹ뺀 길이 = 배열의 인덱스
                result[len(heights)] = index + 1
                break

    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!