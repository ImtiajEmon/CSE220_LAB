'''
Topics, in no particular order:
1. Creating an array
2. Iterating over the elements of an array
3. Copying an array
4. Resizing an array
5. Reversing an array
6. Shifing an array left
7. Shifing an array right
8. Inserting an element into an array
9. Removing an element from an array
10. Rotating an array left
11. Rotating an array right
'''
#==============================================================

def Print(a):
    for i in a:
        print(i,end=' ')
    print("\n")

def Copy(a):
    copied_arr = []
    for i in a:
        copied_arr.append(i)
    return copied_arr

def Resize(a):
    print("In python list is a dynamic array. So, you don't have to worry about size. Keep going.")

def Reverse(a):
    reversed_arr = []
    for i in range(len(a) - 1, -1, -1):
        reversed_arr.append(a[i])
    return reversed_arr

def left_shift(a):
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = 0
    return a

def right_shift(a):
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = 0
    return a

def Insert(a, index, value):
    new_arr = []
    right_part = a[0 : index]
    left_part = a[index : len(a)]
    new_arr = right_part
    new_arr.append(value)
    new_arr += left_part
    return new_arr

def Remove(a, index):
    new_arr = []
    right_part = a[0 : index]
    left_part = a[index+1 : len(a)]
    new_arr = right_part + left_part
    return new_arr

def left_rotate(a):
    frst_value = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = frst_value
    return a

def right_rotate(a):
    last_value = a[len(a) - 1]
    for i in range(len(a) - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = last_value
    return a

def Sort(a):
     n = len(a)
     
     for i in range(n):
         for j in range(0, n-i-1):
             if a[j] > a[j+1] :
                 a[j], a[j+1] = a[j+1], a[j]

#1
arr = [5, 20, 35, 12, 50, 100]

#2
Print(arr)

#3
arr2 = Copy(arr)
print("copied array:")
Print(arr2)

#4
Resize(arr)

#5
arr = Reverse(arr)
print("reversed array:")
Print(arr)

#6
arr = left_shift(arr)
print("after left shift:")
Print(arr)

#7
arr = right_shift(arr)
print("after right shift:")
Print(arr)

#8
arr = Insert(arr, 2, 99) # array.insert(index, value)
print("after insertion:")
Print(arr)

#9
arr = Remove(arr, 1) # remove by index
print("after remove:")
Print(arr)

#10
arr = left_rotate(arr)
print("after left rotation")
Print(arr)

#11
arr = right_rotate(arr)
print("after right rotation")
Print(arr)

#sort
Sort(arr)
print("After sort: ")
Print(arr)
