def find(n):
    for a in range(1, n):
        for b in range(0, n) :
            if a**2+b**2 == (n - a - b)**2 :
                return (a, b, n-a-b)
    return (-1, -1, -1)

print(find(1000))