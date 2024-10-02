class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def appendleft(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head.next = new_node
        else:
            new_node.next = self.head
            self.head.next = new_node
        self.length += 1

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head.next = new_node

        else:
            current = self.head
            while current is not None:
                current = current.next
            current.next = new_node

    def __str__(self):
        if self.head is None:
            return False

        else:
            res = "Head"
            current = self.head
            while current is not None:
                res += "->" + str(current.data)
                current = current.next
        return res

    def __contains__(self, target):
        if self.head is None:
            return False

        else:
            current = self.head
            while current is not None:
                if current.data == target:
                    return True
                current = current.next
            return False

    def popleft(self):
        if self.head is None:
            return None
        else:
            current = self.head
            self.head = self.head.next
            self.length -= 1
        return current.data

    def pop(self):
        if self.head is None:
            return None

        else:
            current = self.head
            while current is not None:
                prev = current
                current = current.next

            if current == self.head: #마지막까지 왔는데 current와 head는 같은 노드의 주소를 할당
                self.head = None

            else :
                prev.next = None #하나 있을 때 이 코드가 왜 안되냐면 prev도 첫번째 노드의 주소를 할당받기 때문
            self.length -= 1
            return current.data
