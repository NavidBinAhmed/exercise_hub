'''
Problem Statement: Prime Numbers:  
Write a Python script to find the first 1,000 prime numbers.  

Procedure:
2) The result will be kept in dictionary variable named “prime_dict” and kept in the file named “prime.txt”  

3) The dictionary prime_dict has the string-type keys “1”, “2”, “3”, … and there should be no keys without element.  

4) The dictionary prime_dict has the list-type values 
[2,3,5,7], [11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97], [101,103,107,...,991,997], 

… associated with keys “1”, “2”, “3”, …, respectively. 

That is the key is the number of digits of the prime numbers.  

5) The list of values must be sorted.  

6) The file “prime.txt” shall have the format exactly like this.  

7) Three dots at the end indicate that there are more lines. 
1:2,3,5,7 2:11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97 …  

7) Before the program ends, print the value of prime_dict using print(prime_dict).
'''


import os


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True

    #logic apply
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def find_primes_up_to_n(n):
    #prime numbers up to a specific range
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def write_primes_to_file(prime_dict, filename):
    with open(filename, 'w') as file:
        for key in sorted(prime_dict):
            primes = ','.join(map(str, prime_dict[key]))
            file.write(f"{key}:{primes}\n")

def main():
    prime_dict = {}
    primes = find_primes_up_to_n(7919)   

#1000 prime nunbers takes it to 7919
    
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
