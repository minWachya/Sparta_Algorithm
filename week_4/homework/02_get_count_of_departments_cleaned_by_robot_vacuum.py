current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# amp = 0 : 청소 안 한 장소, 1 : 청소 못 하는 장소, 2 : 청소한 장소
# 북 동 남 서
# 위 오른쪽 아래 왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)       # 행 갯수
    m = len(room_map[0])    # 열 갯수
    count_of_departments_cleaned = 1  # 청소하는 칸의 개수
    room_map[r][c] = 2      # 현재 장소는 청소한 상태로 변경
    queue = list([[r, c, d]])   # 청소할 위치와 다음에 청소할 방향 큐에 담기

    # 큐가 비어지면 종료
    while queue:
        r, c, d = queue.pop(0)
        temp_d = d

        # 4방향 청소하기
        for i in range(4):
            # 방향 전환
            temp_d = get_d_index_when_rotate_to_left(temp_d)
            # 다음에 이동할 위치
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]

            # 새로운 위치가 맵 밖을 벗어나지 않고 청소를 안 했다면
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count_of_departments_cleaned += 1   # 청소한 횟수 ++
                room_map[new_r][new_c] = 2          # 청소하기
                queue.append([new_r, new_c, temp_d])# 큐에 담아서 다음에 위치 청소하게 하기
                break

            # 더이상 갈 곳이 없었던 경우
            elif i == 3:
                # 후진하기
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[get_d_index_when_go_back(d)]
                # 후진해서 청소할 곳 있나 찾기 위해 큐에 넣기
                queue.append([new_r, new_c, d])

                # 뒤가 벽인 경우
                if room_map[new_r][new_c] == 1:
                    return count_of_departments_cleaned


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))