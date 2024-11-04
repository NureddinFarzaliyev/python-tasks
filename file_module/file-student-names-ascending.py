a = input("Insert student's name. Type DONE if it's done. \n")
names = []

while a!='DONE':
  names.append(a)
  a = input()

names.sort()

file = open('students.txt', 'w')

for name in names:
  file.write(name + '\n')

print("Student names are written in a txt file named 'students.txt'")
print("Run this command to see content: cat students.txt")