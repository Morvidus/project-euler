# Special Pythagorean triplets, i.e. a<b<c; a^2 + b^2 = c^2

ijh_pairs = []

# First find possible pairs that sum to 1000
for i in range(1, 1000):
    for j in range(1, 1000):
        for h in range(1, 1000):
            if i+j+h == 1000:
                if i<j and j<h:
                    if i**2 + j**2 == h**2:
                        subarr = [i, j, h]
                        print(subarr)
                        ijh_pairs.append(subarr)

print(ijh_pairs)
