def digit_fifth_powers():

    fifth = [d**5 for d in range(10)]
    upper_bound = 6 * 9**5

    total = 0
    for n in range(2, upper_bound + 1):
        if n == sum(fifth[int(d)] for d in str(n)):
            total += n

    return total

print(digit_fifth_powers())