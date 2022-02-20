cnt = 0
#using loop
'''def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
'''

#using recursion

def bubble_sort(arr, i = 1):
    if i == len(arr):
        return

    for j in range(1, len(arr) - i):
       
        if arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
    
    bubble_sort(arr, i+1)

#arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
arr = [4,2,1,6,3,5]
it = 0

bubble_sort(arr)
print(arr)
#print(p)