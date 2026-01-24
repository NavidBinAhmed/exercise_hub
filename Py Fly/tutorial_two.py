'''write a function that

1. prints the sum of numbers
2. prints the max value
3. prints the min value
4. prints the second largest number
5. prints the reversed number''' 

'''def sum_num(list):

    summation = 0

    for elements in list:
        summation += elements

    return summation

list = [1,2,3]
print(sum_num(list))'''

'''def max_value(list):

    maximum = 0

    for elements in list:
        if elements >= maximum:
            maximum = elements
    
    return maximum

list = [1,2,3,6,4,7]
print(max_value(list))'''

'''def min_value(list):

    minimum = float('inf')

    for elements in list:
        if elements <= minimum:
            minimum = elements

    return minimum

list = [7,2,3,4]
print(min_value(list))'''


'''def second_largest(list_input):


    first, second = float('-inf'), float('-inf')

#[1,2,3]--for 1 in list: if 1 > -inf, 
    for elements in list_input:
        if elements > first:
            second = first
            first = elements

#[1,2,4,3]--- 4 > 3 > new sec
        elif first > elements > second:
            second = elements

    return second

print(second_largest(list_input=[1,2,3,4,5,6,7,8]))'''


'''def reversed_number(list_input):

    reversed_list = []

    for elements in list_input[::-1]:
        reversed_list.append(elements)

    return reversed_list

given_list = [1,2,43,21,4,2]
print(reversed_number(given_list)) '''

#sum
'''def summation(input_list):
    sum_input = 0

    for elements in input_list:
        sum_input += elements
    return sum_input

given_list = [1,2,3,4,5] 
print(summation(given_list))'''

#leetcode palindrome problem
'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 :
            return False
        
        number = x
        reverse = 0

        while number:
            reverse = reverse * 10 + number % 10
            number //= 10

        return x == reverse
    
check = Solution()
print(check.isPalindrome(-121))'''
    
#leetcode fibonacci
'''class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n-2) + self.fib(n-1)
    
series = Solution()
        
print(series.fib(40))'''


'''class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

series = Solution()
print(series.fib(1000))'''


'''def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(10000))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]'''


'''def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Calculate the 1,000,000th Fibonacci number
fib_1000000 = fib(1000000)
#print("The calculation is done successfully.")
'''
