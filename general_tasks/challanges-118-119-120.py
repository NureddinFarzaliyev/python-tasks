import random

class challange118:
    def __init__(self):
        self.num = 0

    def countToNum(self):
        self.num = int(input("Enter number: \n"))
        for i in range(0, self.num + 1):
            print(i)

class challange119:
    def __init__(self):
        self.low = 0
        self.high = 0
        self.guess = 0
        self.comp_num = 0

    def pickLowAndHigh(self):
        self.low = int(input("Pick low number\n"))
        self.high = int(input("Pick high number\n"))
        self.comp_num = random.randint(self.low + 1, self.high - 1)

    def makeGuess(self):
        print("I am thinking of a number...")
        self.guess = int(input("Take a guess! \n"))

    def checkGuess(self):
        while self.guess != self.comp_num:
            if self.guess > self.comp_num:
                print("You're too high")
            else:
                print("You're too low")
            self.guess = int(input("Take another guess.\n"))
        print("Correct! \n")


def challange120():
    anumber1 = random.randint(6, 19)
    anumber2 = random.randint(6, 19)
    addition = anumber1 + anumber2
    snumber1 = random.randint(26, 49)
    snumber2 = random.randint(1, 25)
    subtraction = snumber1 - snumber2

    choice = int(input("1) Additon\n2) Subtraction\nEnter 1 or 2: \n"))
    if choice == 1:
        add_choice = int(input("What is " + str(anumber1) + "+" + str(anumber2) + "= "))
        print("Your answer: " + str(add_choice) + ", " + "Correct Answer: " + str(addition))
        print("Your answer is " + str(add_choice == addition))
    elif choice == 2:
        sub_choice = int(input("What is " + str(snumber1) + "-" + str(snumber2) + "= "))
        print("Your answer: " + str(sub_choice) + ", " + "Correct Answer: " + str(subtraction))
        print("Your answer is " + str(sub_choice == subtraction))

        


# challange118.countToNum(challange118)

# challange119.pickLowAndHigh(challange119)
# challange119.makeGuess(challange119)
# challange119.checkGuess(challange119)

# challange120()
