name = "John"
age = 25
balance = 1234.56
city = "New York"

print("{} is {} years old, has a balance of ${:.2f} in his account, and lives in {}.".format(name, age, balance, city))
print(f"{name} is {age} years old, has a balance of ${balance:.2f} in his account, and lives in {city}.")
print("%s is %d years old, has a balance of $%.2f in his account, and lives in %s." % (name, age, balance, city))
