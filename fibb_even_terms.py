# Euler Fibonacci

N = 4000000

sequence = [1,2]
prev_ind1 = 0
prev_ind2 = 1

sum_nums = 0

while (sequence[prev_ind1]+sequence[prev_ind2]) < N:    
    prev_ind1 = len(sequence) - 1
    prev_ind2 = len(sequence) - 2
    sequence.append(sequence[prev_ind1]+sequence[prev_ind2])

for number in sequence:
    if number % 2 == 0:
        sum_nums += number

print(sum_nums)
