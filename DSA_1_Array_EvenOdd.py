# Array: write a function to segregate even odd numbers

# approach 1: partition array

def even_odd(arr):
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


'''repeat'''
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

'''repeat'''
def even_odd_segregated(arr):

    ans_list = []

    for i in range(len(arr)):
        if arr[i]%2==0:
            ans_list.append(arr[i])

    for j in range(len(arr)):
        if arr[j]%2 != 0:
            ans_list.append(arr[j])
    
    return ans_list

# driver code
arr = [1,2,3,4,5,6,7,8,0]
result = even_odd_segregated(arr)
print(f"The segregated list: {result}")