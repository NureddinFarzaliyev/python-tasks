from cli import CommandLineInterface
CLI = CommandLineInterface()

def main():
    CLI.start()
    while True:
        command = input("Enter command: ")
        CLI.execute(command)

main()
