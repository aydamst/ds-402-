class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListArray:
    def __init__(self):
        self.head = None

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index < 0:
            raise ValueError("Invalid index")
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise ValueError("Invalid index")
                current = current.next
            if current is None:
                raise ValueError("Invalid index")
            new_node.next = current.next
            current.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_at_index(self, index):
        if index < 0 or self.head is None:
            raise ValueError("Invalid index")
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                raise ValueError("Invalid index")
            current = current.next
        if current.next is None:
            raise ValueError("Invalid index")
        data = current.next.data
        current.next = current.next.next
        return data

    def get_at_index(self, index):
        if index < 0 or self.head is None:
            raise ValueError("Invalid index")
        current = self.head
        for _ in range(index):
            if current is None:
                raise ValueError("Invalid index")
            current = current.next
        if current is None:
            raise ValueError("Invalid index")
        return current.data

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(elements)