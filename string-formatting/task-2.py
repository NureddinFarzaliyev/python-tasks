fullname = input("What is your full name?")
number = len(fullname.replace(" ", ""))

answer = f"Hello, {fullname}! There are {number} letters on your name."

with open("file.csv", "a") as f:
    f.write(f"task2, {answer}\n")
