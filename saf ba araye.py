class Queue:
    def __init__(self):
        self.queue = []  # نگهداری عناصر صف

    def is_empty(self):
        return len(self.queue) == 0  #بررسی خالی بودن

    def enqueue(self, item):
        self.queue.append(item)  # اضافه کردن عنصر جدید

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"  
        return self.queue.pop(0)  #حذف و بازگرداندن عنصر ابتدای صف

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]  # بازگرداندن عنصر ابتدای صف

    def size(self):
        return len(self.queue)  # بازگرداندن تعداد عناصر

    def reverse_queue(self):
        self.queue = self.queue[::-1]  # برعکس کردن لیست صف
        return self.queue  # بازگرداندن لیست صف برعکس شده