num = int(input("Enter the number of people: "))
people = []

for i in range(num):
    name = input(f"Enter the name of the person {i + 1}: ")
    age = int(input("Enter the age of the person: "))
    score = int(input("Enter the score of the person: "))
    people.append([name, age, score])

    people.sort(key=lambda person: (person[0], person[1], person[2]))

print(people)