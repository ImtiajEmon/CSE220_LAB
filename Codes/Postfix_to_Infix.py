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
        return self.iterator + 1
#==================================================

def to_infix(postfix):
    infix = ""
    st = stack()

    for element in postfix:
        if element == '+' or element == '-' or element == '*' or element == '/' or element == '%':
            infix = element + st.pop() + ')'
            infix = '(' + st.pop() + infix
            st.push(infix)

        else:
            st.push(element)

    infix = st.pop()
    return infix

postfix = "259%+2-62-+2/36*8-1++"
print(to_infix(postfix))
