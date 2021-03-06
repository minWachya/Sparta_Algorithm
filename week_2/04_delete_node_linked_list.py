class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # 삽입
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 접근
    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # 추가
    def add_node(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    # 삭제
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index - 1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.add_node(2, 3)
linked_list.add_node(0, 0)
linked_list.print_all()
#print(linked_list.get_node(1).data) # -> 5를 들고 있는 노드를 반환해야 합니다!