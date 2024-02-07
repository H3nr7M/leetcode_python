class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise Exception("Queue is empty")
        return self.stack2.pop()

# create a new Queue object
q = Queue()

# enqueue some items into the queue
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# dequeue an item from the queue and print it
print(q.dequeue())  # output: 1

# enqueue another item
q.enqueue(4)

# dequeue all remaining items and print them
print(q.dequeue())  # output: 2
print(q.dequeue())  # output: 3
print(q.dequeue())  # output: 4

# try to dequeue from an empty queue (should raise an exception)
try:
    q.dequeue()
except Exception as e:
    print(str(e))  # output: Queue is empty