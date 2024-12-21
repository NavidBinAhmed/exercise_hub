'''### Beginner
1. Find the maximum and minimum element in an array.
_2. Reverse an array.
_3. Find the sum of all elements in an array.
_4. Find the average of all elements in an array.
_5. Check if an array contains a specific element.

### Intermediate
_1. Find the second largest element in an array.
_2. Remove duplicates from an array.
_3. Rotate an array by `k` positions.
_4. Find the intersection of two arrays.
_5. Merge two sorted arrays.

### Advanced
1. Find the subarray with the maximum sum (Kadane's Algorithm).
2. Find the longest increasing subsequence in an array.
3. Find the majority element in an array (element that appears more than n/2 times).
4. Find the smallest subarray with a sum greater than a given value.
5. Find the number of subarrays with a given XOR.

You can start solving these problems one by one to improve your understanding of array data structures.'''

# Time complexity = big O of n = O(n)
def reverse_array(arr):
    return arr[::-1]

arr = [1,2,3,4,5]
result = reverse_array(arr)
print(f"The reversed of the given array: {result}")


def reverse_of_list(arr):
    return arr[::-1]

arr = [1,2,3,4,5]
result = reverse_of_list(arr)
print(f"Revised: {result}")

#.....................................#

# Time complexity = O(n)
def find_max_min(arr):
    max_element = max(arr)
    min_element = min(arr)
    return max_element, min_element

arr = [1, 2, 3, 4, 5]
max_element, min_element = find_max_min(arr)
print(f"Maximum element: {max_element}, Minimum element: {min_element}")

def max_min(arr):
    max_element_2 = max(arr)
    min_element_2 = min(arr)
    return max_element_2, min_element_2

arr = [1,2,6,8,4,7,3,7]
max_element_2, min_element_2 = max_min(arr)
print(f"max is {max_element_2}, min is {min_element_2}")

#.....................................#

# Time complexity = O(n)
def contains_element(arr, element):
    return element in arr

arr = [1, 2, 3, 4, 5]
element = 3
result = contains_element(arr, element)
print(f"Array contains {element}: {result}")


def is_element(arr, target):
    return target in arr

arr = [1,3,2,4,6,4,6]
target = 10
result = is_element(arr, target)
print(f"Array contains {target}: {result}")

#.....................................#

# Time complexity = O(n)
def find_second_largest(arr):
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

arr = [1, 2, 3, 4, 5]
result = find_second_largest(arr)
print(f"Second largest element: {result}")


def sec_largest(arr):
    first, second = float('-inf'), float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

arr = [1,2,4,3,6,4,8,9,4]
result = sec_largest(arr)
print(f"The second largest element: {result}")

#.....................................#

# Time complexity = O(n)
def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)
print(f"Array after removing duplicates: {result}")


def duplicates_removal(arr):
    return list(set(arr))

arr = [1,2,2,9,9,9,4,5,6,6,4,4]
result= duplicates_removal(arr)
print(f"Revised arr after removal: {result}")

#.....................................#

# Time complexity = O(n)
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
k = 2
result = rotate_array(arr, k)
print(f"Array after rotating by {k} positions: {result}")


def rotation_of_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [0,1,2,3,4,5,6,7,8,9]
k = 4
result = rotation_of_array(arr, k)
print(f"The rotated array: {result}")
#.....................................#

# Time complexity = O(n + m)
def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
result = find_intersection(arr1, arr2)
print(f"Intersection of arrays: {result}")


def intersec(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1,2,3,6,7,8]
arr2 = [1,4,7,9,0,5]
result = intersec(arr1, arr2)
print(f"The common elements: {result}")
#.....................................#

# Time complexity = O(n + m)
def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
result = merge_sorted_arrays(arr1, arr2)
print(f"Merged sorted arrays: {result}")



def merge_array(arr1, arr2):
    return arr1 + arr2, set(arr1 + arr2), list(set(arr1 + arr2))

arr1= [1,0,2]
arr2 = [4,5,6]
result = merge_array(arr1,arr2)
print(f"Merged array: {result}")
#.....................................#

# Time complexity = big O of n = O(n)
def sum_element(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
arr = [1,2,3,4,5]
result = sum_element(arr)
print("Sum of element in the array:", result)

def addition(array):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    return sum

array = [3,5,1,7,8,4]
result = addition(array)
print(f"addition of {array} is: {result}")

def summation_element(arr):
    sum = 0
    for elements in range(len(arr)):
        sum = sum + arr[elements]
    return sum

#driver code
arr = [1,2,4,6,3,6]
result = summation_element(arr)
print(f"Summation of the elements in given array {arr} is {result}")
#.....................................#

#  Time complexity = big O of n = O(n)
def average_element(arr):
    avg = 0
    for i in range(len(arr)):
        avg = sum(arr)/len(arr)
    return avg

arr = [5,4,3,6,7,5,3]
result = average_element(arr)
print("Average of element in the array:", result)


def avg_elem(arr):
    return sum(arr), len(arr), sum(arr)/len(arr)

arr = [1,2,3,4,5,9]
result = avg_elem(arr)
print(f"avg is {result}")

#.....................................#

# fibonacci problem
def sum_of_fibonacci(n):
    a, b = 0, 1
    sum_fib = a
    for _ in range(1, n):
        a, b = b, a + b
        sum_fib += a
    return sum_fib

n = 10
result = sum_of_fibonacci(n)
print(f"The sum of the first {n} Fibonacci numbers is: {result}")

'''nth fib and sum of n fib numbers'''
def sum_fib(n):
    a, b = 0, 1
    #summation = 0
    for _ in range(1, n):
        a, b = b, a+b
#        summation = summation + a
#    return summation
    return a

'''0 1 1 2 3 5 8'''
n = 5
result = sum_fib(n)
print(f"The {n}th fib number: {result}")

def fibonacci_O(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
result = fibonacci_O(10)
print("The 10th fibonacci number is:", result)

'''optimize the code for fibonacci problem using recursion''' 
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


'''0 1 1 2 3 5 8 13 21 34'''
def fib_opt(n):
    if n <=1:
        return n
    elif n>1:
        return fib_opt(n-1) + fib_opt(n-2)
n = 9
result = fib_opt(n)
print(f"the {n}th fib: {result}")