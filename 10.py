def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_prime(n):
    x = 0
    for i in range(2, n):
        if is_prime(i) :
            x+=i
    return x

print(sum_of_prime(2000000))