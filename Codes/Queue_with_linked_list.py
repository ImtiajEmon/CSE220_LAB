class Node():
    def __init__(self, key, nxt = None):
        self.key = key
        self.next = nxt

class Queue():
    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, key):
        new_node = Node(key)

        if self.front == None:
            self.front = new_node
            self.back = new_node

        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        temp = self.front.key
        temp_node = self.front

        self.front = self.front.next
        temp_node.key = None
        temp_node.next = None

        return temp

    def peek(self):
        return self.front.key

q = Queue()
q.enqueue(10)
q.enqueue(30)
q.enqueue(20)

q.dequeue()
print(q.peek())