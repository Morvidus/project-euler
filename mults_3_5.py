# Proj Euler - Mults of 3 & 5

N = 1000
sum_nums = 0;

for i in range(N):
    if i%3 == 0:
        sum_nums = sum_nums + i
    elif i%5 == 0:
        sum_nums = sum_nums + i

print(sum_nums)
        
