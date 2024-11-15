menu = ' 1) Make a code \n 2) Decode a message \n 3) Quit  \n Enter Selection:'
running = 1

def code(text, number, param):
    result = ""
    
    for char in text:
        if char.isalpha(): 
            if char.isupper():
                ascii = 65 
            else: 
                ascii = 97
            if(param == 'code'):
                shifted_char = chr(((ord(char) - ascii + number) % 26) + ascii)
            elif(param == 'decode'):
                shifted_char = chr(((ord(char) - ascii - number) % 26) + ascii)
            result += shifted_char
        else:
            result += char
    
    return result

while(running):
    opt = int(input(menu))

    match opt:
        case 1:
            text = input("Please input text to be decoded:")
            number = int(input("Please input the number:"))
            print(code(text, number, "code"))
        case 2:
            text = input("Please input text to be decoded:")
            number = int(input("Please input the number:"))
            print(code(text, number, "decode"))
        case 3:
            running = 0