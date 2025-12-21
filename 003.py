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


print(prime_factors(600851475143)[-1])