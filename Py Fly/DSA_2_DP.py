# Fibonacci using DP memoization, time complexity = O(n)
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


# practice
def fib_memo(n, memo = {}):
    if n in memo:
        return memo[n]
    
    elif n <= 1:
        return n
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

n = 10
result = fib_memo(n)
print(f"The {n}th Fibonacci number using memoization (practice) is: {result}")

# Fibonacci using recursion, time complexity = O(2^n).
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
n = 10
result = fib(n)
print(f"The {n}th Fibonacci number using recursion is: {result}")



# Fibonacci using DP tabulation, time complexity = O(n)
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