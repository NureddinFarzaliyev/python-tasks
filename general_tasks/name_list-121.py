running = 1
menu = '1. Display Names\n2. Add New Name\n3. Edit a Name\n4. Delete a Name\n0. Exit'
names = ['a', 'b']

def printMenu():
    print('\n-------------\n')
    print(menu)
    print('\n-------------\n')
    ch = int(input("Choose an option: "))
    return ch

def displayNames():
    print("\nNames:\n")
    for i in range(0, len(names)):
        print(str(i+1) + '.' , names[i])

def addNewName():
    new = input("Type New Name: ")
    names.append(str(new))
    print("Name " + new + " appended to the list.")

def editName():
    displayNames()
    index = int(input("\nWhich item do you want to edit? "))
    new = str(input("Type the new name for " + names[index - 1] + " "))
    names[index - 1] = new
    print("Name is successfully changed to " + names[index - 1])

def deleteName():
    displayNames()
    index = int(input("\nWhich item do you want to delete? "))
    names.remove(names[index - 1])
    print("Name deleted successfully")

while (running == 1):

    ch = printMenu()

    match ch:
        case 1:
            displayNames()
        case 2: 
            addNewName()
        case 3: 
            editName()
        case 4: 
            deleteName()
        case 0:
            print("Program stopped. Final list: \n")
            displayNames()
            running = 0
        case _:
            print("\nPlease enter valid option.")