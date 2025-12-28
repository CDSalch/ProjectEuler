def name_value(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

def total_name_scores(filename="names.txt"):

    with open(filename, "r") as f:
        names = f.read().replace('"', '').split(',')
    
    names.sort()
    
    score = sum((i + 1) * name_value(name) for i, name in enumerate(names))
    
    return score

print(total_name_scores("names.txt"))