def BinarySearch(arr, i, j, target):

    if j >= i:
        mid = i + (j-i)//2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            return BinarySearch(arr, mid+1, j, target)
        
        else:
            arr[mid] > target
            return BinarySearch(arr, i, mid-1, target)

    return -1

# driver code
arr = [12, 56, 78, 88, 89, 91, 96]
i = 0
j = len(arr) - 1
target = 89

result = BinarySearch(arr, i, j, target)
print(f"Target lies in {result}th index.")