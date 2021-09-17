'''
Name: MD IMTIAJ HOSSAIN
ID: 19201031
Sec: 08'''

class Node():
    def __init__(self, e, n):
        self.element = e
        self.next = n

class MyList():
    def __init__(self, arr):
        self.head = None
        tail = None

        for element in arr:
            n = Node(element, None)

            if self.head == None:
                self.head = n
                tail = n
            else:
                tail.next = n
                tail = n


    def showList(self):
        if self.head == None:
            print("Empty List")
            return
        temp = self.head
        
        while temp != None:
            if temp.next == None:
                print(temp.element)
            else:
                print(temp.element, end = " -> ")
            temp = temp.next

    
    def isEmpty(self):
        if self.head == None:
            return True
        return False


    def clear(self):
        self.head = None


    def insert(self, New_element):
        exist = False
        temp = self.head
        tail = None

        while temp != None:
            if temp.element == New_element:
                exist = True
            tail = temp
            temp = temp.next

        if exist:
            print("The key already exist!")
        else:
            tail.next = Node(New_element, None)


    def length(self):
        len = 0
        temp = self.head

        while temp != None:
            len += 1
            temp = temp.next

        return len
        #recursive
        #node = self.head
        #if node == None:
            #return 0
        #return 1 + self.length(node.next)


    def insert_at_indx(self, New_element, index):
        if index < 0 or index > self.length():
            print("Invalid Index!")
            return

        temp = self.head

        c = 0
        while temp != None:
            if c == index and temp.element == New_element:
                print("The key value already exist!")
                return
            c += 1
            temp = temp.next

        if index == 0:
            n = Node(New_element, self.head)
            self.head = n

        c = 0
        temp = self.head
        while temp != None:
            if c == index - 1:
                post_node = temp.next
                temp.next = Node(New_element, post_node)
            c += 1
            temp = temp.next

    def remove(self, value):
        temp = self.head

        if temp.element == value:
            self.head = temp.next
            return value

        while temp.next != None:
            if temp.next.element == value:
                temp.next = temp.next.next
                return value
            temp = temp.next



#=============== Task - 3  ===================

    def even_element(self):
        head = None
        tail = None
        temp = self.head

        #creating list
        while temp != None:
            if temp.element % 2 == 0:
                n = Node(temp.element, None)

                if head == None:
                    head = n
                    tail = n
                else:   
                    tail.next = n
                    tail = n
            temp = temp.next

        #printing
        temp = head
        while temp != None:
            if temp.next != None:
                print(temp.element, end = " -> ")
            else:
                print(temp.element)
            temp = temp.next


    def isMember(self, element):
        temp = self.head

        while temp != None:
            if temp.element == element:
                return True
            temp = temp.next
    
        return False


    def reverse(self):
        newHead = None
        n = self.head

        while(n is not None):
            nextNode = n.next
            n.next = newHead
            newHead = n
            n = nextNode

        self.head = newHead
        lst.showList()


    def sort(self):
        i = self.head

        while i != None:
            j = i
            while j != None:
                if i.element > j.element:
                    i.element, j.element = j.element, i.element
                j = j.next
            i = i.next

    def sum_of(self):
        temp = self.head
        sum = 0

        while temp != None:
            sum += temp.element
            temp = temp.next

        print(sum)



    def rotate(self, type, k):
        size = self.length()
        k = k % size

        if k % size == 0:
            self.showList()
            return

        tail = self.head
    
        #finding tail
        while tail.next != None:
            tail = tail.next

        #join the tail with head
        tail.next = self.head

        #typewise operation
        if type == "left":
            temp = self.head
            for i in range(k - 1):
                temp = temp.next
            self.head = temp.next
            temp.next = None

        else:
            temp = self.head
            for i in range(size - k-1):
                temp = temp.next
            
            self.head = temp.next
            temp.next = None

        self.showList()


#=================================================
#Task-2.1

arr = [10, 45, 30, 40, 50]
lst = MyList(arr)

#Task-2.2
#lst.showList()

#Task-2.3
#print(lst.isEmpty())

#Task-2.4
#lst.clear()

#Task-2.5
#lst.insert(40)

#Task-2.6
#lst.insert_at_indx(45, 1)
#lst.showList()

#Task-2.7
#print(lst.remove(10))
#lst.showList()

#================= Task 3 ======================
#Task-3.1
#lst.even_element()

#Task-3.2
#print(lst.isMember(48))

#Task-3.3
#lst.reverse()

#Task-3.4
#lst.sort()
#lst.showList()

#Task-3.5
#lst.sum_of()

#Task-3.6
#lst.rotate("left", 2)
#lst.rotate("right", 5)

print(lst.length())