# find 10001st prime
import numpy as np

def isPrime(num):
    if num <= 1 or num % 1 > 0:
        return False
#    if num == 4:
#        return False
    for i in range(2, num//2):
        if(num%i == 0):
            return False
    return True

prime_count = 6
i = 2
count = 0

while count != prime_count:
    if isPrime(i) == True:
        count += 1
    i += 1

print("\n")
print(count)
print(i-1)
