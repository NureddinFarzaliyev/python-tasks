str = input("Input string: ")
lower = 0; upper = 0

for i in str:
    if i.isalpha():
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1

print(f"UPPER CASE {upper}\nLOWER CASE {lower}")