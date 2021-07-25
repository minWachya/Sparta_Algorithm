# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    # 큐이 비지 않을 때까지 반복
    while queue:
        # 맨 앞 노드 꺼내기
        current_node = queue.pop(0)
        # 방문 기록 남기기
        visited.append(current_node)

        # 현재 노드에 인접한 노드들 접근
        for adjacent_node in adj_graph[current_node]:
            # 가보지 않은 곳이면 방문하기
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!