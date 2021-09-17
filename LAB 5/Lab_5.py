'''
Name: MD IMTIAJ HOSSAIN
ID  : 19201031
Sec : 08'''
# Task 1 ==================================
# a).
def factorial(n):
    if n == 0:  
        return 1
    return n * factorial(n-1)

# b).
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# c).
def print_array(arr, idx = 0):
    if len(arr) == 0:
        print("The array is empty!")
        return

    if idx == len(arr) - 1:
        print(arr[idx])
        return

    print(arr[idx], end = ', ')
    return print_array(arr, idx+1)

# d).
def power(a, n):
    if n == 0:
        return 1
    
    return a * power(a, n-1)
#================================================

# Task 2=========================================
# a).
def to_binary(n):
    if n == 0 or n == 1:
        return str(n)

    return to_binary(n // 2) + str(n % 2)

# b).
class Node():
    def __init__(self, ele, nxt):
        self.element = ele
        self.next = nxt

def creat_list(arr):
        head = None
        tail = None

        for i in arr:
            new_node = Node(i, None)

            if head == None:
                head = new_node
                tail = new_node

            else:
                tail.next = new_node
                tail = new_node

        return head

def add_element(head):
    if head is None:
        return "This list is empty!"

    if head.next == None:
        return head.element

    return head.element + add_element(head.next)

# c).
def reverse_print(head):
    if head == None:
        print("This list is empty!")
        return

    if head.next == None:
        print(head.element)
        return

    reverse_print(head.next)
    print(head.element)
#================================================

# Task 3=========================================
def num_of_cards(height):
    if height == 0:
        return 0

    if height == 1:
        return 8

    return 5 + num_of_cards(height-1)
#================================================

# Task 5=========================================
# a).
def print_column(column):  #it prints the column number
    if column == 0:
        return ''

    return print_column(column - 1) + str(column) + ' '

def pattern1(n, row = 1):
    if row > n:
        return

    print(print_column(row))
    return pattern1(n, row + 1)


# b).
def print_num(column):
    if column == 0:
        return ''

    return print_num(column - 1) + str(column) + ' '

def print_space(column):
    if column == 0:
        return ''

    return print_space(column - 1) + '  '

def pattern2(n, row = 1):
    if row > n:
        return

    print(print_space(n - row), end = '')
    print(print_num(row))
    return pattern2(n, row + 1)
#================================================

# Task 6=========================================

class FinalQ:
    def print(self,array,idx):
        if(idx<len(array)):
            profit = self.calcProfit(array[idx]) #TO DO
            print(f"{idx + 1}. Investment: {array[idx]}; Profit: {profit}")
            self.print(array, idx + 1) 

    def calcProfit(self,investment):
        if investment <= 25000:
            return 0

        x1 = (100000 - 25000) / 1000 # x1 is basically the investment below 100K / 1000 
        profit_of_x1 = self.multiply(x1, 45)

        if investment <= 100000:
            return profit_of_x1  # I multiply the percentage by 1000 to get floor value, (4.5/100)*1000=45

        x2 = (investment - 100000) / 1000 # x2 is basically the investment above 100K / 1000
        return profit_of_x1 + self.multiply(x2, 80)

    def multiply(self, x, y):
        if y == 1:
            return x
        
        return x + self.multiply(x, y-1)

#================================================

'''Tester'''
# 1.a
#print(factorial(8))

# 1.b
print(fibonacci(10))

# 1.c
#arr = [10, 20, 30, 40]
#print_array(arr)

# 1.d
#print(power(10, 9))

# 2.a
#print(to_binary(7))

# 2.b
#arr = [10, 20, 30, 40]
#head = creat_list(arr)
#print(add_element(head))

# 2.c
#arr = [10, 20, 30, 40]
#head = creat_list(arr)
#reverse_print(head)

# 3
#print(num_of_cards(3))

# 5.a)
#pattern1(5)

# 5.b)
#pattern2(9)

# 6
#array=[25000,100000,250000,350000]
#f = FinalQ()
#f.print(array,0)