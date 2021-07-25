k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 짝수면 +1더한 방향, 홀수면 -1한 방향으로 바꾸기
def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1  # 게임 턴
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]  # 체스판 위에 말 위치 배열
    # ex)current_stacked_horse_map[r][c] = [0, 1, 2] : (r, c)위치에 체스 말 0, 1, 2이 있다
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            n = len(game_map)
            # 각 말의 위치, 이동 방향 꺼내기
            r, c, d = horse_location_and_directions[horse_index]
            # 각 말의 이동 방향에 대해 새로운 위치 만들기
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 3) 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다.
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]
                # 3) 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

                    # 같이 이동할 말 배열
                    moving_horse_index_array = []
                    for i in range(len(current_stacked_horse_map[r][c])):
                        current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                        # 여기서 이동해야 하는 애들은 현재 옮기는 말 위의!!! 말들이다.
                        if horse_index == current_stacked_horse_index:
                            moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                            current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]
                            break

                    # 2) 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
                    if game_map[new_r][new_c] == 1:
                        moving_horse_index_array = reversed(moving_horse_index_array)

                    # 이동한 말들 새로운 위치에 넣어주기
                    for moving_horse_index in moving_horse_index_array:
                        current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                        # horse_location_and_directions 에 이동한 말들의 위치를 업데이트한다.
                        horse_location_and_directions[moving_horse_index][0], \
                        horse_location_and_directions[moving_horse_index][
                            1] = new_r, new_c

                    # 말이 4개 이상 쌓이면 종료
                    if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                        return turn_count

                # 턴 카운트++
                turn_count += 1

            return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
        [0, 1, 0],
        [1, 1, 0],
        [0, 2, 0],
        [2, 2, 2]
    ]
print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

start_horse_location_and_directions = [
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 0],
        [2, 1, 2]
    ]
print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))
