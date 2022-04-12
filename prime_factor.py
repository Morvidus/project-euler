# Euler prime factors

N = 600851475143
i=2

# largest prime factor will never be > sqrt(n), add 1 to i until then
while i*i <= N:
    #while i divides evenly into n, replace n with n/i
    while N%i == 0:
        N = N/i
    i += 1
        
print(N)
