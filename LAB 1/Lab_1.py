'''
Name: MD IMTIAJ HOSSAIN
Id: 19201031
Sec: 08 
'''

#task-1
def shiftLeft(source, k):
    i = 0
    while(i+k < len(source)):
        source[i] = source[i+k]
        i += 1

    while(i < len(source)):
        source[i] = 0
        i += 1

#task-2
def rotateLeft(source, k):
    temp_arr = [0] * k
    for i in range(0, k):
        temp_arr[i] = source[i]

    i = 0
    while(i+k < len(source)):
        source[i] = source[i+k]
        i += 1

    j = 0
    while(i < len(source)):
        source[i] = temp_arr[j]
        i += 1
        j += 1

#task-3
def remove(source, size, index):
    if(index < 0 or index > len(source)):
        print("Wrong index!")
        return
    if(index == size-1):
        source[index] = 0
        return

    indx = index
    for i in range(index, size-1):
        source[i] = source[i+1]
        indx = i
    
    #if size == len(source):
    source[indx+1] = 0

#task-4
def removeAll(source, size, element):
    #for i in range (0, size):
    i = 0
    while(i < size):
        if(source[i] == element):
            for j in range(i, size):
                source[j] = source[j+1]
            i -= 1
        i += 1

#task-5
def splitting_arr(source):
    ans = False
    sum = 0

    pref_sum = [0] * len(source)
    for i in range(0, len(source)):
        sum += source[i]
        pref_sum[i] = sum

    for i in pref_sum:
        if i == sum-i:
            ans = True
            break
    print(ans) 

#task-6
def arr_series(n):
    arr = [0] * (n*n)

    indx = 0
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if j <= i:
                arr[indx] = j
            else:
                arr[indx] = 0
            indx += 1
    return arr

#task-7
def bunch_count(arr):
    cnt = 0
    temp_cnt = 1

    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            temp_cnt += 1
        else:
            cnt = max(cnt, temp_cnt)
            temp_cnt = 1
    
    cnt = max(cnt, temp_cnt)
    if cnt == 1:
        return 0
    return cnt

#task-8
def repetition(arr):
    max_element = 0
    for i in arr:
        max_element = max(max_element, i)
    
    cnt_arr = [0] * (max_element + 1)
    for i in arr:
        cnt_arr[i] += 1

    repet_arr = [0] * len(arr)
    idx = 0
    for i in cnt_arr:
        if i > 1:
            for j in repet_arr:
                if j == i:
                    return True
            repet_arr[idx] = i
            idx += 1
    return False

#Circular Array
#task-1
def check_palindrome(arr, size, start):
    i = start
    j = size + start - 1

    while(i < j):
        if(arr[i % len(arr)] != arr[j % len(arr)]):
            return False
        i += 1
        j -= 1

    return True

#task-2
def intersection(arr1, size1, start1, arr2, size2, start2):
    new_arr = [0] * min(size1, size2)
    cnt = 0
    indx = 0
    indx1 = start1
    
    for i in range(0, size1):
        indx2 = start2
        for j in range(0, size2):
            if arr1[indx1] == arr2[indx2]:
                new_arr[indx] = arr1[indx1]
                cnt += 1
                indx += 1
            indx2 = (indx2 + 1) % len(arr2)
        indx1 = (indx1 + 1) % len(arr1)

    ret_arr = [0] * cnt
    for i in range(0, cnt):
        ret_arr[i] = new_arr[i]

    return ret_arr

#task-3
def chair_game():
    import random
    players = ["Tahmid", "Ifty", "Asif", "Tahsin", "Sadman", "Rifat", "Pial"]
    size = 7

    while size != 1:
        a = random.randint(0, 3)
        if a == 0 or a == 2 or a == 3:
            rotateLeft(players, 1)
        if a == 1:
            if players[size//2] != 0:
                players[size//2] = 0  
                size -= 1  
            
        #print(a, size)
        #print(players)
        s = 1
        for i in range(len(players)):
            if players[i] != 0:
                if(s == size):
                    print(players[i], end = "\n")
                else:
                    print(players[i], end = ", ")
                s += 1
        print()
        

'''
source=[10,20,30,40,50,60]
shiftLeft(source, 3)
print(source)'''

'''
source=[10,20,30,40,50,60]
rotateLeft(source, 3)
print(source)'''

'''
source=[10,20,30,40,50,0,0]
remove(source, 5, 2)
print(source)'''

'''
source=[10,2,30,2,50,2,2,60,0,0]
removeAll(source,8,2)
print(source)'''

'''
source = [10, 3, 10, 2, 1] 
splitting_arr(source)'''

#print(arr_series(3))

'''
source = [1,1,2, 2, 1, 1,1,1] 
print(bunch_count(source))'''

'''
source = [4,5,6,6,4,3,6,4]
print(repetition(source))'''

'''
source =  [10,20,0,0,0,10,20,30]
print(check_palindrome(source, 5, 5))'''

'''
source1 = [40,50,0,0,0,10,20,30]
source2 =  [10,20,5,0,0,0,0,0,5,40,15,25]
print(intersection(source1, 5, 5, source2, 7, 8))'''

#chair_game()