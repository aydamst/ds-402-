class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def remove_node_at_end(self):
        if self.head is None:
            raise ValueError("List is empty")
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next != self.head:
            current = current.next
        data = current.next.data
        current.next = self.head
        return data

    def remove_node_at_begin(self):
        if self.head is None:
            raise ValueError("List is empty")
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next != self.head:
            current = current.next
        data = self.head.data
        current.next = self.head.next
        self.head = self.head.next
        return data

    def display(self):
        elements = []
        if self.head is None:
            print(elements)
            return
        current = self.head
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        print(elements)