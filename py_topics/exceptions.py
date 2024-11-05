def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Not an integer") 

def main():
    x = get_int("X: ")
    y = get_int("Y: ")
    print(x+y)

main()