from itertools import chain

def collatz(n):
    if n == 1 :
        return [1]
    else : 
        if n%2 == 0:
            return list(chain([n], collatz(n//2)))
        else : 
            return list(chain([n], collatz(3*n+1)))
    
def find_longest(n) :
    max = 1
    k = 1
    for i in range(1, n) :
        k0 = len(collatz(i))
        if max < k0 :
            k = i 
            max = k0
    return k

print(find_longest(1000000))