class Queue():
    def __init__(self):
        self.q = []
        self.front = 0
        self.back = -1

    def enqueue(self, key):
        self.q.append(key)
        self.back += 1

    def dequeue(self):
        temp = self.q[self.front]
        self.q.pop(self.front)
        self.back -= 1
        return temp

    def peek(self):
        return self.q[self.front]

'''
q = Queue()
q.enqueue(10)
q.enqueue(30)
q.enqueue(20)
q.dequeue()
print(q.peek())'''