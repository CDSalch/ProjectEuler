def cycle_length(d):
    s = {}
    r = 1 % d
    pos = 0

    while r != 0 and r not in s:
        s[r] = pos
        r = (r * 10) % d
        pos += 1

    if r == 0:
        return 0  
    return pos - s[r]

def longest_recurring_cycle(limit=1000):
    max_len = 0
    result = 0

    for d in range(2, limit):
        length = cycle_length(d)
        if length > max_len:
            max_len = length
            result = d

    return result, max_len

result, max_len = longest_recurring_cycle(1000)
print(result)
