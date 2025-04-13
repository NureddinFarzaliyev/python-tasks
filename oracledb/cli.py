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
            "status": self.status
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
        print("Available commands:")
        print("- connect")
        print("- disconnect")
        print("- create_table")
        print("- show_all_tables")
        print("- show_table_rows")
        print("- insert_row")
        print("- delete_row")

    def exit(self):
        print("Exiting CLI...")
        DB.disconnect()
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
        tables = DB.show_all_tables()
        for table in tables:
            print(table[0])

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

    def execute(self, command):
        if command in self.commands:
            self.commands[command]()
        else:
            self.invalid()
