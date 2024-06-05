class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.items)

# Exercise 1: Enqueue elements to the queue
queue1 = Queue()
queue1.enqueue(10)
queue1.enqueue(20)
queue1.enqueue(30)
print("Exercise 1: Enqueue elements")
print("Queue after enqueuing:", queue1.items)

# Exercise 2: Dequeue an element from the queue
queue2 = Queue()
queue2.enqueue(10)
queue2.enqueue(20)
queue2.enqueue(30)
dequeued_item = queue2.dequeue()
print("Exercise 2: Dequeue an element")
print("Dequeued item:", dequeued_item)
print("Queue after dequeueing:", queue2.items)

# Exercise 3: Peek at the front element of the queue
queue3 = Queue()
queue3.enqueue(10)
queue3.enqueue(20)
queue3.enqueue(30)
peeked_item = queue3.peek()
print("Exercise 3: Peek at the front element")
print("Peeked item:", peeked_item)
print("Queue after peeking:", queue3.items)

# Exercise 4: Check if the queue is empty
queue4 = Queue()
print("Exercise 4: Check if the queue is empty")
print("Is the queue empty initially?", queue4.is_empty())
queue4.enqueue(10)
queue4.enqueue(20)
print("Is the queue empty after enqueuing elements?", queue4.is_empty())

# Exercise 5: Get the size of the queue
queue5 = Queue()
print("Exercise 5: Get the size of the queue")
print("Initial queue size:", queue5.size())
queue5.enqueue(10)
queue5.enqueue(20)
queue5.enqueue(30)
print("Queue size after enqueuing elements:", queue5.size())
queue5.dequeue()
print("Queue size after dequeuing an element:", queue5.size())
