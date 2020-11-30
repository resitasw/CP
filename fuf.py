from collections import defaultdict
import math

# 1. Get Prime Factorization of a Number
# Source
# https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f
def get_prime_factors(number):

    prime_factors = defaultdict(int)

    while number % 2 == 0:
        prime_factors[2]+=1
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            prime_factors[i] += 1
            number = number / i

    if number > 2:
        prime_factors[number]+=1

    return prime_factors