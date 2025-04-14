import datetime
from db import DatabaseConnection
DB = DatabaseConnection()

class CommandLineInterface:
    pass

    def __init__(self):
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "connect": self.connect,
            "disconnect": self.disconnect,
            "create_table": self.create_table,
            "show_all_tables": self.show_all_tables,
            "show_table_rows": self.show_table_rows,
            "insert_row": self.insert_row,
            "delete_row": self.delete_row,
            "status": self.status,
            "log": self.log,
            "log_csv": self.log_csv
        }

    def start(self):
        print("Welcome to the CLI to manage employees!")
        print("Enter 'help' for a list of commands.")
        print("Enter 'exit' to quit.")

    def status(self):
        if DB.status():
            print("Connected to the OracleDB")
        else:
            print("Not connected to the OracleDB")

    def help(self):
        print("You can use the commands below to interact with the Database:")
        for command in self.commands.keys():
            print(f"- {command}")

    def exit(self):
        print("Exiting CLI...")
        exit()

    def connect(self):
        DB.connect()

    def disconnect(self):
        DB.disconnect()

    def create_table(self):
        table_name = input("Enter table name: ")
        columns = input("Enter columns (comma-separated): ").split(",")
        DB.create_table(table_name, columns)

    def show_all_tables(self):
        DB.show_all_tables()

    def show_table_rows(self):
        table_name = input("Enter table name: ")
        DB.show_table_rows(table_name)

    def insert_row(self):
        table_name = input("Enter table name: ")
        values = input("Enter values (comma-separated): ").split(",")
        DB.insert_row(table_name, values)

    def delete_row(self):
        table_name = input("Enter table name: ")
        filter_column = input("Enter filter column: ")
        filter_value = input("Enter filter value: ")
        DB.delete_row(table_name, filter_column, filter_value)

    def invalid(self):
        print("Invalid command!")

    def log(self):
        n = int(input("Enter the number of logs you want to see: "))
        with open('operationLog.log', 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line.strip())

    def log_csv(self):
        fileName = f"operationLog-{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv"
        try:
            with open("operationLog.log", 'r') as f:
                        lines = f.readlines()

            with open(fileName, 'w') as csv:
                for line in lines:
                    csv.write(line.replace(" ", ","))

            print(f"CSV file saved as {fileName}")
        except FileNotFoundError:
                print("Log file not found")
        except Exception as e:
            print(f"An error occurred: {e}")
    def execute(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            self.invalid()
