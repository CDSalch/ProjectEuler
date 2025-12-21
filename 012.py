from collections import Counter

def prime_factors(n):
    if n < 2:
        return []  

    factors = []
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factors.append(n)

    return factors


def number_of_divisors(n):
    if n < 1:
        return 0

    factors = prime_factors(n)
    counts = Counter(factors)

    total = 1
    for exp in counts.values():
        total *= (exp + 1)

    return total

def find(n):
    i = 2
    k = 1
    while number_of_divisors(k) < n :
        k +=i
        i += 1
    return k    

print(find(500))