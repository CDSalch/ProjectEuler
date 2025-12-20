n = 1000

def sum_of_square(n) :
    return n*(n+1)*(2*n+1)/6

def square_of_sum(n):
    k = n*(n+1)/2
    return k**2
    
def difference(n):
    return square_of_sum(n) - sum_of_square(n)

print(difference(n))