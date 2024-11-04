menu = '1. Add to File\n2. View all Records\n3. Delete a record\n4. Quit Program'
running = 1

def printMenu():
    print('\n-------------\n')
    print(menu)
    print('\n-------------\n')
    ch = int(input("Choose an option: "))
    return ch

file = open('salaries.csv', 'a+')

def writeOnFile(name, salary):
    file.seek(0)
    if(file.read() == ""):
        file.write("name, salary\n")
    file.seek(0, 2)
    file.write(name + ", " + salary + "\n")

def addOnFile():
    name = str(input("Please input name: "))
    salary = str(input("Please input salary: "))
    writeOnFile(name, salary)
    print("\nFile updated.\n")

def displayFile():
    file.seek(0)
    print("\n")
    print(file.read())

def removeFromFile():
    file.seek(0)
    lines = file.readlines()
    for i in range(0, len(lines)):
        print(str(i) + ") " + lines[i].replace('\n', ''))
    index = int(input("Type in the index of the record you want to delete."))
    lines.remove(lines[index])
    file.truncate(0)
    file.writelines(lines)

while(running == 1):
    ch = printMenu()

    match ch:
        case 1:
            addOnFile()
        case 2:
            displayFile()
        case 3:
            removeFromFile()
        case 4:
            running = 0

file.close()