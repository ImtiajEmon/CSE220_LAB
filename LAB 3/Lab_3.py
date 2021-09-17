'''
Name: MD IMTIAJ HOSSAIN
ID: 19201031
Sec: 08'''

class Node():
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList():
    def __init__(self, arr):
        self.head = Node(None, None,None)
        tail = self.head

        for element in arr:
            new_node = Node(element, None, tail)
            #new_node.prev = tail
            tail.next = new_node
            tail = tail.next
        tail.next = self.head
        self.head.prev = tail

    def showList(self):
        curr_node = self.head.next

        if curr_node == self.head:
            print("Empty List!")
            return

        #Forward printing
        while curr_node != self.head:
            if curr_node.next == self.head:
                print(curr_node.element)
            else:
                print(curr_node.element, end = " <-> ")
            curr_node = curr_node.next

        '''#Backward printing
        curr_node = self.head.prev
        while curr_node != self.head:
            if curr_node.prev == self.head:
                print(curr_node.element)
            else:
                print(curr_node.element, end = " <-> ")
            curr_node = curr_node.prev'''


    def size(self):
        curr_node = self.head.next

        s = 0
        while curr_node != self.head:
            s += 1
            curr_node = curr_node.next
        return s

    
    def insert(self, new_element, index  = None):
        curr_node = self.head.next

        while curr_node != self.head:
            if curr_node.element == new_element:
                print("Already exist!")
                return
            curr_node = curr_node.next

        if index == None:
            new_node = Node(new_element, self.head, self.head.prev)
            self.head.prev.next = new_node
            self.head.prev = new_node
            return

        if index < 0 or index > self.size():
            print("Invalid index!")
            return

        curr_node = self.head.next
        for i in range(index):
            curr_node = curr_node.next

        new_node = Node(new_element, curr_node, curr_node.prev)
        curr_node.prev.next = new_node
        curr_node.prev = new_node


    '''
    def deletekey(self, key):
        temp = self.head.next
        while temp != self.head:
            if temp.element == key:
                (temp.next).prev = temp.prev
                (temp.prev).next = temp.next
            temp = temp.next'''

    '''
    def insert(self, value):
        tail = self.head.next
        while tail.next != self.head:
            if tail.element == value:
                return
            tail = tail.next

        n = Node(value, None, None)
        n.next = self.head
        n.prev = tail
        tail.next = n
        self.head.prev = n'''


    def remove(self, index):
        if index < 0 or index > self.size() - 1:
            print("Invalid index!")
            return

        curr_node = self.head.next
        for i in range(index):
            curr_node = curr_node.next

        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev

    
    def removeKey(self, deletekey):
        curr_node = self.head.next

        cnt = 0
        while curr_node.element != deletekey:
            curr_node = curr_node.next
            cnt += 1
            if cnt == self.size():
                print("Absent deletekey!")
                return deletekey

        curr_node.prev.next = curr_node.next
        curr_node.next.prev = curr_node.prev
        return deletekey

    
    

arr = [10, 20, 30, 40]
lst = DoublyList(arr)

#Task - 2.2
#lst.showList()

#Task-2.3 & Task-2.4
#lst.insert(50)
#lst.insert(50, 3)
#lst.showList()

#Task-2.5
#lst.remove(2)
#lst.showList()

#Task-2.6
#print(lst.removeKey(10))
#lst.showList()