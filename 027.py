def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def quadratic_primes(n):
    max = 0
    best = 0

    primes_b = [b for b in range(2, n+1) if is_prime(b)]

    for a in range(1-n, n, 2):  
        for b in primes_b:
            k= 0
            while is_prime(k*k + a*k + b):
                k += 1

            if k > max:
                max = k
                best = a * b

    return best


print(quadratic_primes(1000))
