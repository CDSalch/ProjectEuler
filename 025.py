def num_digits(n):
    return len(str(abs(n)))

def find(n) :
    k, l, m = 0, 1, 0 
    i = 0
    while True : 
        m = k
        k = l
        l += m
        i+=1
        if num_digits(k) == n :
            return (k, i)

F_index, index = find(1000)      
print(index)