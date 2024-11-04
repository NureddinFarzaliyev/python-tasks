def checkAnd(input1, input2):
    if input1 == 'false' or input2 == 'false':
        return False
    else:
        return True

def checkOr(input1, input2):
    if input1 == 'true' or input2 == 'true':
        return True
    else:
        return False

input1 = input("Input 1: ").lower()
input2 = input("Input 2: ").lower()

file = open('andor_result.txt', 'w')

file.write("And: " + str(checkAnd(input1, input2)) + "\n")
file.write("Or: " + str(checkOr(input1, input2)) + "\n")

print("Data saved on andor_result.txt")