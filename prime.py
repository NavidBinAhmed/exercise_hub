import os

def is_prime(num):
    """ Check if a number is prime """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_up_to_n(n):
    """ Find prime numbers up to n """
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def write_primes_to_file(prime_dict, filename):
    """ Write prime numbers organized by digit length to a file """
    with open(filename, 'w') as file:
        for key in sorted(prime_dict):
            primes = ','.join(map(str, prime_dict[key]))
            file.write(f"{key}:{primes}\n")

def main():
    prime_dict = {}
    primes = find_primes_up_to_n(7919)  # Finding primes up to 7919 (approximate 1000th prime)
    
    for prime in primes:
        digit_length = len(str(prime))
        if digit_length not in prime_dict:
            prime_dict[digit_length] = []
        prime_dict[digit_length].append(prime)
    
    for key in prime_dict:
        prime_dict[key].sort()

    write_primes_to_file(prime_dict, "prime.txt")
    
    print(prime_dict)

if __name__ == "__main__":
    main()
