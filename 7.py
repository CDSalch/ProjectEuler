def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find(n):
    k = 1
    i = 0
    
    while i<n:
        k+=1
        if is_prime(k):
            i+=1
    
    return k
    
    
    
print(find(10001))