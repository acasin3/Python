# What is the largest prime factor of the number 600851475143?

import math

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n + 1))):
        if n % i == 0:
            return False
    return True

def largest_prime(n):
    max = math.ceil(math.sqrt(n))
    while max > 1 :
        if n % max == 0 and is_prime(max) == True:
            break
        else:
            max -= 1

    return max

print(largest_prime(600851475143))

