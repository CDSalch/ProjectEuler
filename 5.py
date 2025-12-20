def smallest_divisible_by (n) :
    flag = True
    i = n
    while flag :
        flag = False
        for k in range(2, n):
            if i%k !=0 :
                flag = True
                i += 1
                break
        
    return i

print(smallest_divisible_by(20))