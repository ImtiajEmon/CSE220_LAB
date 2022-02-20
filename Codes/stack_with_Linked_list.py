class Node():
    def __init__(self, element, prev):
        self.element = element
        self.prev = prev

class stack():
    #prev = None
    top = None

    def push(self, element):
        self.top = Node(element, self.top)

    def peak(self):
        return self.top.element

    def pop(self):
        top_node = self.top
        self.top = self.top.prev
        value = top_node.element
        top_node.element = None
        top_node.prev = None
        return value


st = stack()
'''
st.push(5)
st.push(10)
st.push(15)
print(st.pop())
print(st.peak())
print(st.size())'''
st.push(15)
print(st.pop())
print(st.peak())