'''reversal of an array'''
# approach 1: slicing operation for reversal of an array

list = [2,4,5,7,8,9]

operation_1 = list[::-1]
''' 
: = starting index
: = ending index
-1 = step size (1 element from opposite side)
'''

print(operation_1)

operation_2 = list[::]
'''start and ending index as it is.
it will print the same input list.'''

print(operation_2)

operation_3 = list[::-2]
'''should print [9,7,4], every other element from reverse direction.
as ::-2, this -2 indicates the reversal'''

print(operation_3)

operation_4 = list[::2]
'''start and end indexes are as it is.
every other element from input array. [2,5,8]'''
print(operation_4)

operation_5 = list[2:4]
'''it will take the index of 2 which is 5.
Upto the index of 1 less than 4 which is 3, that is 7.
Output will be [5,7]'''
print(operation_5)

operation_6 = list[5::-1]
print(operation_6)
# Time complexity = big O of n = O(n)
# Space complexity = big O of 1 = O(1) - no extra space taken


# approach 2: negative indexing in function for reversal of an array
'''writing a function to reverse a list of numbers in an array'''

def reverse_list(array):
    # initialization of empty reversed list
    # as a list of n elements as extra space
    reversed_list = []

    # logic building
    for index in range(1, len(array) +1):
        reversed_list.append(array[-index])
    return reversed_list

# driver code
array =[1,2,3,4,5,6,7,8,9]
# function calling
result = reverse_list(array)
print(f"Reversal of the array: {result}")

'''repeat'''
def reversal(arr):
    # as a list of n elements - extra space
    reversed_list_init = []

    for index in range(1, len(arr) + 1):
        reversed_list_init.append(arr[-index])
    return reversed_list_init

arr = [1,2,3,4,5,6]
result = reversal(arr)
print(f"Reversed: {result}")

# Time complexity = big O of n = O(n)
# Space complexity = big O of n = O(n ) - extra space of implement



# approach 3: two pointers for reversal of array
def reverse_list(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        # Swap the elements at the left and right pointers
        nums[left], nums[right] = nums[right], nums[left]
        # Move the pointers towards the center
        left += 1
        right -= 1
    
    return nums

nums = [1,2,3,4,5,6,7]
result = reverse_list(nums)
print("The reversed list using 2P:", result)

'''repeat two pointers'''
def reverse_list_2p(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# driver code
arr = [1,2,3,4,5,6,7,8]
result = reverse_list_2p(arr)
print("Reversed using 2p:", result)

# time complexity: O(n)
# space complexity: O(1)

'''repeat'''
def reverse_list_2p(arr):
    n = len(arr)
    i = 0
    j = n-1
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i+1
        j = j-1
    return arr

arr= [-1, 0,1,2,3,4,5,6,7,8]
result = reverse_list_2p(arr)
print(f"Reversed list: {result}")