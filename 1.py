
def is_multiple(x, n) : #Check if x is multiple of n
    return (x%n == 0)

def sum_multiple(a, b, n) :
    x = 0
    for i in range(2, n) :
        if (is_multiple(i, a) | is_multiple(i, b)) :
            x += i
    return x

print(sum_multiple(3, 5, 1000))