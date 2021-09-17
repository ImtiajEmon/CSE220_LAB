'''
Name: MD IMTIAJ HOSSAIN
ID: 19201031
Sec: 08'''
#=======================================
#Task - 01 ==> array based stack <==
'''
class stack():
    def __init__(self):
        self.stack = []
        self.iterator = -1

    def push(self, element):
        self.stack.append(element)
        self.iterator += 1

    def peak(self):
        if self.iterator == -1:
            return None
        return self.stack[self.iterator]

    def pop(self):
        if self.iterator == -1:
            return None

        value = self.stack[self.iterator]
        self.stack = self.stack[:self.iterator]
        self.iterator -= 1
        return value

    def size(self):
        return self.iterator + 1'''
#====================================================

#Task - 02 ==> linked list based stack <==
class Node():
    def __init__(self, element, prev):
        self.element = element
        self.prev = prev

class stack():
    top = None
    length = 0

    def push(self, element):
        self.top = Node(element, self.top)
        self.length += 1

    def peak(self):
        return self.top.element

    def pop(self):
        top_node = self.top
        self.top = self.top.prev
        value = top_node.element
        top_node.element = None
        top_node.prev = None
        self.length -= 1
        return value

    def size(self):
        return self.length
        
#==================================================
#tester
def check_parenthesis(expression):
    st = stack()

    for element in expression:
        if element == '(' or element == '{' or element == '[':
            st.push(element)

        elif element == ')' or element == '}' or element == ']':
            if element == ')':
                ele_in_st_should_be = '('
            elif element == '}':
                ele_in_st_should_be = '{'
            elif element == ']':
                ele_in_st_should_be = '['

            if st.size() == 0:
                print("This expression is NOT correct.")
                return
            
            if st.peak() == ele_in_st_should_be:
                st.pop()

            else:
                print("This expression is NOT correct.")
                return

    if st.size() != 0:
        print("This expression is NOT correct.")
        return

    print("This expression is correct.")
        
expression = input()
check_parenthesis(expression)