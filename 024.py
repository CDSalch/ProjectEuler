from math import factorial

def lexicographic_permutation(n, d):

    n -= 1  
    d = list(d)
    result = []

    while d:
        f = factorial(len(d) - 1)
        index = n // f
        result.append(str(d.pop(index)))
        n %= f

    return ''.join(result)

print(lexicographic_permutation(1000000, range(10)))
