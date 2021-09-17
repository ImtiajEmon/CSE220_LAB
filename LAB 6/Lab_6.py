'''
Name: MD IMTIAJ HOSSAIN
ID  : 19201031
Sec : 08'''
# Task 1 (Selection Sort)=======================
def min_index(arr, it, min_idx):
    if it == len(arr):
        return min_idx

    if arr[it] < arr[min_idx]:
        min_idx = it
    return min_index(arr, it+1, min_idx)

def selection_sort(arr, it):
    if it == len(arr):
        return

    min_idx = min_index(arr, it, it) #it gives the index of min value
    
    arr[it], arr[min_idx] = arr[min_idx], arr[it]
    return selection_sort(arr, it+1)
        

# Task 2(Insertion sort)==========================
def insertion_sort(arr, i = 1):
    if i == len(arr):
        return

    j = i - 1
    current = arr[i]
    while j >= 0 and arr[j] > current:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = current

    return insertion_sort(arr, i+1)


#Task 3 (Sort a singly linked sequential list using bubble sort algorithm)
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

def bubble_sort(lst):
    iterator = lst.head

    while iterator.next != None:
        j = lst.head
        while j.next != None:
            if j.element > j.next.element:
                j.element, j.next.element = j.next.element, j.element
            j = j.next
        iterator = iterator.next

# Task 4 (Sort a singly linked sequential list using selection sort algorithm)
def selection_sort2(lst):
    iterator = lst.head
    while iterator != None:
        min_node = iterator
        j = iterator.next
        while j != None:
            if j.element < min_node.element:
                min_node = j
            j = j.next

        iterator.element, min_node.element = min_node.element, iterator.element
        iterator = iterator.next

# Task 5 (Sort a DOUBLY linked sequential list using insertion sort algorithm)
class Node2():
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList():
    def __init__(self, arr):
        self.head = None
        tail = None

        for element in arr:
            new_node = Node2(element, None, tail)

            if self.head == None:
                self.head = new_node
                tail = new_node
            
            else:
                tail.next = new_node
                tail = new_node


    def showList2(self):
        curr_node = self.head

        if curr_node == None:
            print("Empty List!")
            return

        #Forward printing
        while curr_node != None:
            if curr_node.next == None:
                print(curr_node.element)
            else:
                print(curr_node.element, end = " <-> ")
            curr_node = curr_node.next

def insertion_sort2(lst):
    i = lst.head.next
    while i != None:
        j = i.prev
        current = i.element
        while j != None and j.element > current:
            j.next.element = j.element
            j = j.prev

        if j == None:
            lst.head.element = current
        else:
            j.next.element = current
        i = i.next
    
# Task 6 (Implement binary search algorithm RECURSIVELY) ===
def find(arr, x, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if x > arr[mid]:
        return find(arr, x, mid+1, right)

    elif x < arr[mid]:
        return find(arr, x, left, mid-1)

    return mid

# Task 7 (find the n-th Fibonacci number using memoization)
visited = {}
def fibonacci(n):
    if n < 1:
        return "Wrong input!"

    if n == 1:
        return 0

    if n == 2:
        return 1

    if n in visited:
        return visited[n]
    
    visited[n] = fibonacci(n-1) + fibonacci(n-2)
    return visited[n]
#=============================================================
'''                           Tester                         '''
# 1)
#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#it = 0
#selection_sort(arr, it)
#print(arr)

#2)
#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#insertion_sort(arr)
#print(arr)

#3)
#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#lst = MyList(arr)
#bubble_sort(lst)
#lst.showList()

#4)
#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#lst = MyList(arr)
#selection_sort2(lst)
#lst.showList()

#5)
#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#lst = DoublyList(arr)
#insertion_sort2(lst)
#lst.showList2()

#6)
#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#selection_sort(arr, 0)
#found = find(arr, 21, 0, len(arr)-1)
#if found == -1:
#    print("Not Found!")
#else:
#    print(f"Found at index {found}.")
    
#7)
#print(fibonacci(120))