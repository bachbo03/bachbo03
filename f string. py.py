def formatPhone(n1, n2, n3):
    #formatted = "(" + n1 + ') ' + n2 + '-' + n3
    formatted = f"({n1}) {n2}-{n3}"
    return formatted
print(formatPhone("647", "685", "9456"))

def multiplier(n1, n2):
    product = int(n1) * int(n2)
    return f"multiple of {n1} and {n2} is {product}"
print(multiplier(5,5))

def moneyformat(n1):
    return f"${n1:.2f}"

print(moneyformat(29.13847))

def mon_vert(n1):
    return 