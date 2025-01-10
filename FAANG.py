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


'''2. Check the presence of element in 2D array'''
def searchMatrix(matrix, target):

# count rows
  m = len(matrix)
  if m == 0:
    return False
  
  # count columns
  n = len(matrix[0])
  
  left, right = 0, m*n - 1
  while left <= right:
    mid = left + (right - left)//2
    mid_element = matrix[mid//n][mid%n]
    if target == mid_element:
      return True
    elif target < mid_element:
      right = mid - 1
    else:
      left = mid + 1
  return False

# driver code
matrix = [[1,2,3],
          [5,6,7],
          [9,10,11]]
target = 11
# function calling
result = searchMatrix(matrix, target)
print(result)


'''brute force approach - linear'''
def searcharray(matrix, target):

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == target:
        return True
  return False

# driver code
matrix = [[1,2,3,4],
          [5,6,7,8,],
          [9,10,11,12]]
target = 7
result = searcharray(matrix, target)
print(result)