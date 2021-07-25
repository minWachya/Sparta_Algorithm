input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = []  # 1~len까지 압축했을때 길이 값

    # 1~len/2까지 문자열 나눠보기
    for split_size in range(1, n // 2 + 1):
        compressed = "" # 결괏값

        # string 갯수 단위로 쪼개기 *
        # splited[0] = [a b c a b c a b c a b c d e d e d e d e d e d e]
        # splited[1] = [ab ca bc ab ca bc de de de de de de]
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]

        # 쪼개진 문자열들을 압축할 수 있는지 확인
        count = 1
        for j in range(1, len(splited)):
            prev, cur = splited[j - 1], splited[j]
            # 똑같으면 count++
            if prev == cur:
                count += 1
            # 이전 문자와 다르다면
            else:
                # count가 1보다 크면 압축 가능
                if count > 1:
                    compressed += (str(count) + prev)
                # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
                else:
                    compressed += prev

                count = 1  # 초기화

        # 반복 후 남은 문자열들 처리
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:  # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
            compressed += splited[-1]

        # 문자열 길이 저장
        compression_length_array.append(len(compressed))

    return min(compression_length_array)  # 최솟값 리턴


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))