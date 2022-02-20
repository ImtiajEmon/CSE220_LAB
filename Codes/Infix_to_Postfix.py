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
#========================================================

def to_postfix(infix):
    st = stack()

    post_fix = ""
    for element in infix:
        if element == '+' or element == '-':
            while st.size() != 0 and st.peak() != '(' and st.peak() != '{' and st.peak() != '[':
                post_fix += st.pop()
            st.push(element)
        
        elif element == '*' or element == '/' or element == '%':
            while st.peak() != '+' and st.peak() != '-' and st.peak() != None and st.peak() != '(' and st.peak() != '{' and st.peak() != '[':
                post_fix += st.pop()
                if st.size() == 0:
                    break
            st.push(element)

        elif element == '(' or element == '{' or element == '[':
            st.push(element)

        elif element == ')' or element == '}' or element == ']':
            while st.peak() != '(' and st.peak() != '{' and st.peak() != '[':
                post_fix += st.pop()
            st.pop()

        else:
            post_fix += element

    while st.size() != 0:
        post_fix += st.pop()

    return post_fix



infix = "(2+4)*(9-8+5*2)/2%5"
print(to_postfix(infix))