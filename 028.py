def find(n=1001):
    
    if n % 2 == 0:
        raise ValueError("n must be odd")

    total = 1
    layers = (n - 1) // 2

    for k in range(1, layers + 1):
        side = 2 * k + 1
        total += 4 * side * side - 12 * k

    return total

print(find())