import numpy as np

def isPrime(n):
    if n <= 1 or n % 1 > 0:
        return False
    for i in range(2, n//2):
        if(n%i == 0):
            return False
    return True

def primes_below(n):
    for i in range(1,n):
        if isPrime(i):
            print(i)

n = int(input("\nEnter a number: "))

primes_below(n)
