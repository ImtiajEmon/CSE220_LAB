'''
Name: MD IMTIAJ HOSSAIN
ID  : 19201031
Sec : 08'''
# Task 1 on Key index Searching & Sorting 
class KeyIndex():
    def __init__(self, a):
        self.MIN = 0
        if min(a) < 0:
            # this portion is to handle negetive number
            self.MIN = min(a) * -1

            for i in range(len(a)):
                a[i] += self.MIN

        self.k = [0] * (max(a) + 1)

        for element in a:
            self.k[element] += 1


    def search(self, value):
        if value >= len(self.k) or value < self.MIN * -1:
            return False
            
        if self.MIN != 0:
            value += self.MIN

        if self.k[value] == 0:
            return False
        else:
            return True

    
    def sort(self):
        sorted_arr = []

        for i in range(len(self.k)):
            if self.k[i] > 0:
                for j in range(self.k[i]):
                    sorted_arr.append(i - self.MIN)

        return sorted_arr

# Task 2 on Hashing
def h_function(s):
    sum = 0
    cnt_cons = 0

    for char in s:
        if char.isdigit():
            sum += int(char)
        else:
            if char != 'A' and char != 'E' and char != "I" and char != "O" and char != "U" and char != ' ':
                cnt_cons += 1

    return ((cnt_cons * 24) + sum) % 9


def linear_probing(hash_table, idx, string):
    while hash_table[idx] != 0:
        idx = (idx + 1) % 9

    hash_table[idx] = string

def Hashing(arr):
    hash_table = [0] * 9

    for string in arr:
        idx = h_function(string)
        
        if hash_table[idx] == 0:
            hash_table[idx] = string
        else:
            linear_probing(hash_table, idx, string)

    return hash_table
#===========================================================
'''                   Tester                        '''
# 1)
#arr = [30, 45, 20, 20, 20, 95, -10, 95, 0, -5]
#obj = KeyIndex(arr)
#print(obj.search(20))
#print(obj.sort())

# 2)
#str_arr = ["ST1E89B8A32", "13", "SE3", " "]
#print(Hashing(str_arr))