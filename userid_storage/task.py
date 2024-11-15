menu = ' 1) Create a new User ID \n 2) Change a Password \n 3) Display all User IDs \n 4) Quit \n Enter Selection:'
running = 1

data = {}

def getPoints(password):
    point = 0
    if(len(password)>=8):
        point += 1
    if any(char.isupper() for char in password):
        point += 1
    if any(char.islower() for char in password):
        point += 1
    if any(char.isdigit() for char in password):
        point += 1
    if any(char.isalnum() for char in password):
        point += 1
    return point

def getPassword():
    password = input("Input User Password")
    point = getPoints(password)
    if(point < 3):
        while (point < 3):
            password = input("Your password is weak. Input New Password")
            point = getPoints(password)
    if(point < 5):
        while (point < 5):
            again = input("Your password can be improved. Try again? y/n")
            if(again == 'y' or again == 'Y'):
                password = input("Your password is weak. Input New Password")
                point = getPoints(password)
            else:
                break

    return password

def createUser():
    id = input("Input User Id:")
    if(id in data):
        print("User with this ID already exists")
    else:
        password = getPassword()
        data[id] = password


def changePass():
    id = input("Input User Id:")
    if(id in data):
        password = getPassword()
        data[id] = password
    else:
        print("Please choose correct ID")

while(running):
    opt = int(input(menu))

    match opt:
        case 1:
            createUser()
        case 2:
            changePass()
        case 3:
            print(data)
        case 4:
            running = 0