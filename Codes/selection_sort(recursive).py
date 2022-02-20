# using loop
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
'''

def min_index(arr, it, min_idx):

    if it == len(arr):
        return min_idx

    if arr[it] < arr[min_idx]:
        min_idx = it
    return min_index(arr, it+1, min_idx)

def selection_sort(arr, it):
    if it == len(arr):
        return

    min_idx = min_index(arr, it, it)
    
    arr[it], arr[min_idx] = arr[min_idx], arr[it]
    return selection_sort(arr, it+1)
    '''
        

arr = [13, 25, 0, -4, 7, -1, 18, 9, -6, 21]
#arr = [10, 30, 20, 0, 15]
it = 0
selection_sort(arr)
print(arr)