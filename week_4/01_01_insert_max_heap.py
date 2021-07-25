class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 완전 이진트리의 최대 높이인 O(logN)
    def insert(self, value):
        # 배열 끝에 삽입
        self.items.append(value)
        # 삽입한 위치 인덱스 구하기
        cur_index = len(self.items) - 1

        # 루트 노드까지 반복
        while cur_index > 1:
            # 부모 인덱스 구하기
            parent_index = cur_index // 2

            # 부모 노드 < 자식 노드면 교환
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            # 부모 노드가 더 크면 반복 끝
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!