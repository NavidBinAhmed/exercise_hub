'''def add_large_numbers(num1, num2):
    carry = 0
    result = []
    
    max_len = max(len(num1), len(num2))
    num1 = [0] * (max_len - len(num1)) + num1
    num2 = [0] * (max_len - len(num2)) + num2

    for i in range(max_len - 1, -1, -1):
        total = num1[i] + num2[i] + carry
        carry = total // 10
        result.append(total % 10)
    
    if carry > 0:
        result.append(carry)
    
    result.reverse()
    return result

def fib_last_digits(n, digits):
    if n == 0:
        return [0]
    if n == 1:
        return [1]

    a = [0]
    b = [1]

    for _ in range(2, n + 1):
        next_fib = add_large_numbers(a, b)
        a = b
        b = next_fib
        if len(b) > digits:
            b = b[-digits:]  # Keep only the last `digits` digits
    
    return b

# Calculate the last 4 digits of the 1,000,000th Fibonacci number
last_4_digits = fib_last_digits(1000000)
print(''.join(map(str, last_4_digits)))'''


#Matrix exponentials: fast
'''def matrix_mult(A, B):
    """Multiplies two 2x2 matrices A and B."""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]

def matrix_pow(matrix, n):
    """Raises the matrix to the power of n using exponentiation by squaring."""
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        n //= 2

    return result

def fib(n):
    """Returns the n-th Fibonacci number using matrix exponentiation."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1)
    return result[0][0]

# Calculate the 1,000,000th Fibonacci number
fib_1000000 = fib(1000000)
print(fib_1000000)'''


#array: could not even load
'''def add_large_numbers(num1, num2):
    """Adds two large numbers represented as arrays of digits."""
    carry = 0
    result = []
    len1, len2 = len(num1), len(num2)
    for i in range(max(len1, len2)):
        digit1 = num1[len1 - 1 - i] if i < len1 else 0
        digit2 = num2[len2 - 1 - i] if i < len2 else 0
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(total % 10)
    if carry:
        result.append(carry)
    return result[::-1]

def fib_large(n):
    """Computes the n-th Fibonacci number using array representation for large numbers."""
    if n == 0:
        return [0]
    if n == 1:
        return [1]

    a = [0]
    b = [1]
    for _ in range(2, n + 1):
        c = add_large_numbers(a, b)
        a, b = b, c
    return b

# Calculate the 1,000,000th Fibonacci number
fib_1000000 = fib_large(1000000)
print("".join(map(str, fib_1000000)))  # Convert array of digits to string and print

# Print the last 4 digits of the 1,000,000th Fibonacci number
print("".join(map(str, fib_1000000[-4:])))
'''

#string
'''def add_large_numbers_str(num1, num2):
    """Adds two large numbers represented as strings."""
    carry = 0
    result = []
    len1, len2 = len(num1), len(num2)
    for i in range(max(len1, len2)):
        digit1 = int(num1[len1 - 1 - i]) if i < len1 else 0
        digit2 = int(num2[len2 - 1 - i]) if i < len2 else 0
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])

def fib_large_str(n):
    """Computes the n-th Fibonacci number using string representation for large numbers."""
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    a = "0"
    b = "1"
    for _ in range(2, n + 1):
        c = add_large_numbers_str(a, b)
        a, b = b, c
    return b

# Calculate the 1,000,000th Fibonacci number
fib_1000000_str = fib_large_str(1000000)
print(fib_1000000_str)  # Print the entire number'''

# Print the last 4 digits of the 1,000,000th Fibonacci number
# print(fib_1000000_str[-4:])

#modular arithmetic
'''def fib_large_mod(n, mod=10000):
    """Computes the n-th Fibonacci number using modular arithmetic for the last 4 digits."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = (a + b) % mod
        a, b = b, c
    return b

# Calculate the last 4 digits of the 1,000,000th Fibonacci number
fib_1000000_mod = fib_large_mod(1000000)
print(fib_1000000_mod)'''


#iterative dynamic programming
'''def fib_large(n):
    """Computes the n-th Fibonacci number using arbitrary-precision integers."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return b

# Calculate the 1,000,000th Fibonacci number
fib_1000000 = fib_large(1000000)
print(fib_1000000)
'''

'''def fib_large_mod(n, mod=10**100):
    """Computes the n-th Fibonacci number using modular arithmetic."""
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = (a + b) % mod
        a, b = b, c
    return b

# Calculate the 1,000,000th Fibonacci number with all digits
fib_1000000_mod = fib_large_mod(1000000)
print(fib_1000000_mod)'''

'''
now compare time and space complexity among matrix exponentiation (ok), array representation(not even run), 
string representation (not even run), IDP (ok), modular arithmetic () ?
'''
from decimal import Decimal, getcontext

def fibonacci_fixed_point(n):
    """ Computes the n-th Fibonacci number using fixed-point arithmetic. """
    if n == 0:
        return Decimal('0')
    if n == 1:
        return Decimal('1')
    
    a, b = Decimal('0'), Decimal('1')
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

# Set the precision for Decimal arithmetic
getcontext().prec = 100  # Adjust precision as needed

# Calculate the 1,000,000th Fibonacci number using fixed-point arithmetic
fib_1000000 = fibonacci_fixed_point(1000000)
print(fib_1000000)



