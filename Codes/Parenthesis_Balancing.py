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
                print("Imbalanced parenthesis!1")
                return
            
            if st.peak() == ele_in_st_should_be:
                st.pop()

            else:
                print("Imbalanced parenthesis!2")
                return

    if st.size() != 0:
        print("Imbalanced parenthesis!3")
        return

    print("Balanced parenthesis!")
        
s = input()
check_parenthesis(s)