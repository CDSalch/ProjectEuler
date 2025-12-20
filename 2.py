def sum_even_fibonacci(n) :
    x = 0
    k, l, m = 0, 1, 0 
    while l < n : 
        m = k
        k = l
        l += m
        if (l%2 == 0):
            x +=l
    return x

print(sum_even_fibonacci(4000000))