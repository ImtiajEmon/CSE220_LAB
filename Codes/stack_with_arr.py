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
        return self.iterator+1

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