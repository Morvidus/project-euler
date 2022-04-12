# Euler sum square diff


def sq_sum(num):
    sq_sum = 0
    for i in range (1, num+1):
        sq_sum += (i)**2
    print(sq_sum)
    return sq_sum
    
def sum_sq(num):
    sum_sq = 0
    for i in range(1, num+1):
        sum_sq += (i)
    print(sum_sq**2)
    return sum_sq**2

# Main part
num_range = 100

sum_sq = sum_sq(num_range)
sq_sum = sq_sum(num_range)

print(sum_sq-sq_sum)
