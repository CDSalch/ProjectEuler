def proper_divisors(n):
    if n <= 1:
        return []

    d = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    return d


def is_abundant(n):
    return sum(proper_divisors(n)) > n


def find(limit = 28123):

    abundants = [i for i in range(12, limit + 1) if is_abundant(i)]
    abundant_set = set(abundants)

    total = 0

    for i in range(1, limit + 1):
        flag = False
        for a in abundants:
            if a > i:
                break
            if (i - a) in abundant_set:
                flag = True
                break
        if not flag:
            total += i

    return total

print(find())