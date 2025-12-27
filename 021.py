def proper_divisors(n):
    if n <= 1:
        return [] 

    d = [1] 


    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:  
                d.append(n // i)

    return sorted(d)

def sum_divisors (n):
    seq = proper_divisors(n)
    return sum(seq)

def find(n):
    amicable_sum = 0 
    for a in range(2, n):
        b = sum(proper_divisors(a))
        if b != a and sum(proper_divisors(b)) == a:
            amicable_sum += a
    return amicable_sum

print(find(10000))