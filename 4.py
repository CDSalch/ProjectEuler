def is_palindrome (n) :
    n_str = str(n)
    return n_str == n_str[::-1]

def largest_palindrom():
    for i in range(999, 1,-1) :
        for j in range(999, 1, -1):
            k = i*j
            if is_palindrome(k):
                return k
            
print(largest_palindrom())