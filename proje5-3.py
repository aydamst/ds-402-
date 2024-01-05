class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_node_at_end(self):
        if self.head is None:
            raise ValueError("List is empty")
        if self.head.next is None:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next is not None:
            current = current.next
        data = current.data
        current.prev.next = None
        return data

    def remove_node_at_begin(self):
        if self.head is None:
            raise ValueError("List is empty")
        data = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(elements)