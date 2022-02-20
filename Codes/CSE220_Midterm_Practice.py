# Final practice
class Queue():
    def __init__(self):
        self.q = []
        self.front = 0
        self.back = -1

    def enqueue(self, key):
        self.q.append(key)
        self.back += 1

    def dequeue(self):
        temp = self.q[self.front]
        self.q.pop(self.front)
        self.back -= 1
        return temp

    def peek(self):
        return self.q[self.front]

# 2)
'''
Q = [1, 2, 3, 4, 5, 6, 7, 8]
half = len(Q) // 2
j = half 
q = Queue()

for i in range(half):
    q.enqueue(Q[i])
    q.enqueue(Q[j+i])

print(q.q)

#3)

def is_sub_seq(s1, s2, len_s1, len_s2):
    if len_s1 == 0:
        return True
    if len_s2 == 0:
        return False

    if s1[len_s1-1] != s2[len_s2-1]:
        return is_sub_seq(s1, s2, len_s1, len_s2-1)

    return is_sub_seq(s1, s2, len_s1-1, len_s2-1)


s1 = "= bat"
s2 = "table"

if is_sub_seq(s1, s2, len(s1), len(s2)):
    print("Yes")
else:
    print("No")'''

print((370%100)%10)