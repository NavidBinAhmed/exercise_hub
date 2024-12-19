import boto3

'''### Beginner
1. Find the maximum and minimum element in an array.
_2. Reverse an array.
_3. Find the sum of all elements in an array.
_4. Find the average of all elements in an array.
5. Check if an array contains a specific element.

### Intermediate
1. Find the second largest element in an array.
2. Remove duplicates from an array.
3. Rotate an array by `k` positions.
4. Find the intersection of two arrays.
5. Merge two sorted arrays.

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

# Time complexity = O(n)
def find_max_min(arr):
    max_element = max(arr)
    min_element = min(arr)
    return max_element, min_element

arr = [1, 2, 3, 4, 5]
max_element, min_element = find_max_min(arr)
print(f"Maximum element: {max_element}, Minimum element: {min_element}")

# Time complexity = O(n)
def contains_element(arr, element):
    return element in arr

arr = [1, 2, 3, 4, 5]
element = 3
result = contains_element(arr, element)
print(f"Array contains {element}: {result}")

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

# Time complexity = O(n)
def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(arr)
print(f"Array after removing duplicates: {result}")

# Time complexity = O(n)
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

arr = [1, 2, 3, 4, 5]
k = 2
result = rotate_array(arr, k)
print(f"Array after rotating by {k} positions: {result}")

# Time complexity = O(n + m)
def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
result = find_intersection(arr1, arr2)
print(f"Intersection of arrays: {result}")

# Time complexity = O(n + m)
def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
result = merge_sorted_arrays(arr1, arr2)
print(f"Merged sorted arrays: {result}")

# Time complexity = big O of n = O(n)
def sum_element(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
arr = [1,2,3,4,5]
result = sum_element(arr)
print("Sum of element in the array:", result)

#  Time complexity = big O of n = O(n)
def average_element(arr):
    avg = 0
    for i in range(len(arr)):
        avg = sum(arr)/len(arr)
    return avg

arr = [5,4,3,6,7,5,3]
result = average_element(arr)
print("Average of element in the array:", result)


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


# Optimized Fibonacci using dynamic programming memoization, time complexity = O(n)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

n = 10
result = fibonacci_memo(n)
print(f"The {n}th Fibonacci number using memoization is: {result}")

# Optimized Fibonacci using dynamic programming tabulation, time complexity = O(n)
def fibonacci_tabulation(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

n = 10
result = fibonacci_tabulation(n)
print(f"The {n}th Fibonacci number using tabulation is: {result}")
