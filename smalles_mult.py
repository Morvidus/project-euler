## Proj Euler evenly divisible

def checkDivs(n):
    for divisor in divisors:
        if n % divisor != 0:
            return False
    return True

def scan(n, remainder):
    
    while remainder != 0:
        if checkDivs(n):
            return n
        n += 1

# Main part
divisors = []

for i in range (0,20):
    divisors.append(i+1)

n = 2520
remainder = 1   

# Must be at least as large as for up to 10...

print(scan(n, remainder))
