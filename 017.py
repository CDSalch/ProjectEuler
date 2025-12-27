ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen",
         "sixteen","seventeen","eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def number_to_word(n):
    if n == 1000:
        return "onethousand"
    w = ""
    if n >= 100:
        w += ones[n // 100] + "hundred"
        if n % 100 != 0:
            w += "and"
    n = n % 100
    if n >= 20:
        w += tens[n // 10]
        w += ones[n % 10]
    elif n >= 10:
        w += teens[n - 10]
    else:
        w += ones[n]
    return w

total_letters = sum(len(number_to_word(i)) for i in range(1, 1001))
print(total_letters)
