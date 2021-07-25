# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


# 스택으로 구현
def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []

    # 스택이 비지 않을 때까지 반복
    while stack:
        # 현재 노드 꺼내기
        current_node = stack.pop()
        # 방문 기록 남기기
        visited.append(current_node)

        # 현재 노드에 인접한 노드들 접근
        for adjacent_node in adjacent_graph[current_node]:
            # 가보지 않은 곳이면 방문하기
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!