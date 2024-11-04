num = int(input("Decimal Number: "))
base = int(input("New Base: "))
res = ''
while num != 0:
    k = num % base
    num = num // base
    res = str(k) + res
print(res)