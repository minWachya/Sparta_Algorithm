# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# 딕셔너리로 인접 노드 표현
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
visited = []


# 재귀 함수로 구현
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 방문 기록하기
    visited_array.append(cur_node)

    # 인접 노드 방문하기
    for adjacent_node in adjacent_graph:
        # 방문한 적 없는 노드면 방문하기(탈출 조건 역할)
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!