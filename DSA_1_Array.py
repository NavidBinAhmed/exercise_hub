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



# approach 2: negative indexing in function for reversal of an array
'''writing a function to reverse a list of numbers in an array'''

def reverse_list(array):
    # initialization of empty reversed list
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
    reversed_list_init = []

    for index in range(1, len(arr) + 1):
        reversed_list_init.append(arr[-index])
    return reversed_list_init

arr = [1,2,3,4,5,6]
result = reversal(arr)
print(f"Reversed: {result}")











