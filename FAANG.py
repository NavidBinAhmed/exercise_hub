'''1. find the index of the first infinity from an array'''

'''recursion binary search approach'''
def infsearch(arr, i, j, target):

  if i > j:
    return False

  else:
    mid = i + (j-i)//2

    if target < arr[mid]:
      return infsearch(arr, i, mid-1, target)

    if target > arr[mid]:
      return infsearch(arr, mid+1, j, target)

    else:
      target == arr[mid]
      return mid
  
  return -1

# driver code
arr = [1, 2, 3, 6, 7, 9, float('inf')]
i = 0
j = len(arr)-1
target = float('inf')
result = infsearch(arr, i, j, target)
print(f"Index of the first infinity is {result}")


'''linear approach'''
arr_2 = [1, 2, 3, 6, 7, 9, 12, float('inf'), float('inf')]

target = float('inf')

for i in range(len(arr_2)-1):
  if arr_2[i] == target:
    print(i)