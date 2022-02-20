class Array():
    def __init__(self, *elements):
        self.arr = []
        for i in elements:
            self.arr.append(i)

    
def Print(a):
    for i in a:
        print(i, end=' ')
    print()
            

ar = Array(5, 12, 16, 10)
Print(ar.arr)