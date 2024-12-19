
'''### Beginner
1. Find the maximum and minimum element in an array.
2. Reverse an array.
3. Find the sum of all elements in an array.
4. Find the average of all elements in an array.
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