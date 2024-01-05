class QueueUsingStack:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def is_empty(self):
        return len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0

    def enqueue(self, item):
        self.enqueue_stack.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        
        return self.dequeue_stack.pop()

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) > 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        
        return self.dequeue_stack[-1]

    def size(self):
        return len(self.enqueue_stack) + len(self.dequeue_stack)