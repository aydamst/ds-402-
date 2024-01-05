class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            count = 0
            while count < index - 1 and current is not None:
                current = current.next
                count += 1
            if current is None:
                raise IndexError("Index out of range")
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

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def update_node(self, data, index):
        current = self.head
        count = 0
        while count < index and current is not None:
            current = current.next
            count += 1
        if current is None:
            raise IndexError("Index out of range")
        current.data = data

    def remove_node_at_index(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
        current = self.head
        count = 0
        while count < index - 1 and current is not None:
            current = current.next
            count += 1
        if current is None or current.next is None:
            raise IndexError("Index out of range")
        data = current.next.data
        current.next = current.next.next
        return data

    def remove_node_at_end(self):
        if self.head is None:
            raise ValueError("List is empty")
        data = None
        if self.head.next is None:
            data = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            data = current.next.data
            current.next = None
        return data

    def remove_node_at_begin(self):
        if self.head is None:
            raise ValueError("List is empty")
        data = self.head.data
        self.head = self.head.next
        return data

    def size_of_list(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def concatenate(self, linked_list):
        if self.head is None:
            self.head = linked_list.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = linked_list.head

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(elements)