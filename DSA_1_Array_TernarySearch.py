'''Ternary Search'''

def ts(arr, i, j, target):
    if j < i:
        return False
    else:
        mid1 = i + (j-i)//3 # 0=(8-0)//3 = 2
        mid2 = j - (j-i)//3 # 8 -(8-0)//3 = 6

        if target == arr[mid1]:
            return mid1
        if target == arr[mid2]:
            return mid2
        
        if target < arr[mid1]:
            return ts(arr, i, mid1-1, target)
        
        if target < arr[mid2] and target > arr[mid1]:
            return ts(arr, mid1+1, mid2-1, target)
        
        elif target > arr[mid2]:
            return ts(arr, mid2+1, j, target)
    
    return False

# driver code
#     [0,1,2,3,4,5,6,7,8, 9,10]
arr = [1,2,3,4,5,6,7,8,9,10,11]
i = 0
j = len(arr) - 1
target = 1
result = ts(arr, i, j, target)
print(f"The index is {result}")
