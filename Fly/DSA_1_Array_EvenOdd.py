# Array: write a function to segregate even odd numbers

# approach 1: partition array

'''def even_odd(arr):
    ans_list = []
    
    for numbers in range(len(arr)):
        if arr[numbers]%2==0:
            ans_list.append(arr[numbers])
    for numbers in range(len(arr)):
        if arr[numbers]%2 !=0:
            ans_list.append(arr[numbers])
    return ans_list

# driver code 
arr = [2,7,9,4,8,1]
result = even_odd(arr)
print(f"The segregated even odd numbers: {result}")

# time = O(n)
# space = O(n)


#repeat
def even_odd(arr):
    ans_list = []

    for nums in range(len(arr)):
        if arr[nums]%2==0:
            ans_list.append(arr[nums])
    for nums in range(len(arr)):
        if arr[nums]%2!=0:
            ans_list.append(arr[nums])

    return ans_list

arr = [1,2,3,4,5,6,7]
result = even_odd(arr)
print(f"The segregated even odd: {result}")

# repeat
def even_odd_segregated(arr):

    ans_list = []

    for i in range(len(arr)):
        if arr[i]%2==0:
            ans_list.append(arr[i])

    for j in range(len(arr)):
        if arr[j]%2 == 1:
            ans_list.append(arr[j])
    
    return ans_list

# driver code
arr = [1,2,3,4,5,6,7,8,0]
result = even_odd_segregated(arr)
print(f"The segregated list: {result}")'''


# approach 2: two-pointer appraoch
def even_odd(arr):
    n = len(arr)
    i = -1
    j = 0
    
    while j<n:
        if arr[j]%2==0:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        else: 
            j = j+1 # Move to the next element regardless of even or odd
    return arr

arr = [1,2,3,4,5,6,7,8]
result= even_odd(arr)
print(result)


'''repeat'''
def even_odd(arr):
    n = len(arr)
    i = -1
    j = 0
    while j<n:
    #while j<n:
        if arr[j]%2==0:
            i=i+1
            arr[i], arr[j] = arr[j], arr[i]
        else:
            j = j+1
    return arr

# driver code 
arr = [1,2,3,4,5,6,7,8]
result = even_odd(arr)
print(f"The even-odd separated list: {result}") 

# Time Complexity: O(n)
# Space Complexity: O(1) '''no extra space for an additional initialized list'''