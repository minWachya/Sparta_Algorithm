# 최댓값 힙
# 최댓값의 추가/삭제 및 정렬이 빠르게 이루어짐
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

    # 완전 이진트리의 최대 높이인 O(logN)
    def delete(self):
        # 루트 노드와 마지막 노드 교환
        self.items[1], self.items[-1] = self.items[-1], self.items[1]

        # 최댓값 데이터 저장
        # 데이터 삭제
        delete_date = self.items.pop()

        cur_index = 1
        # 제일 마지막 노드까지 힙 규칙 따르기
        while cur_index <= len(self.items) - 1:
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1

            # 현재 노드 값, 왼쪽 자식 값, 오른쪽 자식 값 중 가장 큰 값의 인덱스
            max_index = cur_index

            # 왼쪽 자식이 존재하고 부모보다 크다면
            if left_index <= len(self.items) - 1 and self.items[left_index] > self.items[max_index]:
                max_index = left_index
            # 오른쪽 자식이 존재하고 부모보다 크다면
            if right_index <= len(self.items) - 1 and self.items[right_index] > self.items[max_index]:
                max_index = right_index

            # 현재 인덱스가 자식보다 크면 반복 종료
            if max_index == cur_index:
                break

            # 현재 값과 가장 큰 값 변경
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]

        return delete_date  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]