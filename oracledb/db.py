import oracledb
import datetime

def createLog(logType, operationType, user, additionalInformation):
    with open('operationLog.log', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} [{logType}] [{operationType}] [{user}] : {additionalInformation} \n")

class DatabaseConnection:
    pass

    # Initialize the database connection
    def __init__(
        self,
        user="system",
        password="123456",
        dsn="localhost:1521/xe"
    ):
        self.user = user
        self.password = password
        self.dsn = dsn
        self.connection = None
        self.cursor = None
        self.isConnected = False

    # Connect to DB
    def connect(self):
        try:
            self.connection = oracledb.connect(
                user=self.user,
                password=self.password,
                dsn=self.dsn
            )
            self.cursor = self.connection.cursor()
            print("Connected to the Oracle Database")
            self.isConnected = True
            createLog("INFO", "CONNECT", self.user, "Connected to the OracleDB")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            createLog("ERROR", "CONNECT", self.user, f"Error connecting to the database: {e}")

    # Disconnect from DB
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Disconnected from the Oracle Database")
        self.isConnected = False
        createLog("INFO", "DISCONNECT", self.user, "Disconnected from the OracleDB")

    # Check if connected
    def status(self):
        return self.isConnected

    # Create a table
    def create_table(self, table_name, columns):
        try:
            if self.cursor:
                self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")
                print(f"Table '{table_name}' created successfully")
                createLog("INFO", "CREATE_TABLE", self.user, f"Table '{table_name}' created successfully")
            else:
                print("Cursor not initialized")
                createLog("ERROR", "CREATE_TABLE", self.user, "Cursor not initialized")
        except Exception as e:
            print(f"Error creating table: {e}")
            createLog("ERROR", "CREATE_TABLE", self.user, f"Error creating table: {e}")

    # Show all tables
    def show_all_tables(self):
        try:
            if self.cursor:
                self.cursor.execute("SELECT table_name FROM user_tables")
                tables = self.cursor.fetchall()
                print("Tables:")
                createLog("INFO", "SHOW_TABLES", self.user, "Tables displayed successfully")
                for table in tables:
                    print(table[0])
            else:
                print("Cursor not initialized")
                createLog("ERROR", "SHOW_TABLES", self.user, "Cursor not initialized")
        except Exception as e:
            print(f"Error displaying tables: {e}")
            createLog("ERROR", "SHOW_TABLES", self.user, f"Error displaying tables: {e}")

    # Show all rows in a table
    def show_table_rows(self, table_name):
        try:
            if self.cursor:
                self.cursor.execute(f"SELECT * FROM {table_name}")
                rows = self.cursor.fetchall()
                print(f"Rows in '{table_name}':")
                createLog("INFO", "SHOW_TABLE_ROWS", self.user, f"Rows in '{table_name}' displayed successfully")
                for row in rows:
                    print(row)
            else:
                print("Cursor not initialized")
                createLog("ERROR", "SHOW_TABLE_ROWS", self.user, "Cursor not initialized")
        except Exception as e:
            print(f"Error displaying rows: {e}")
            createLog("ERROR", "SHOW_TABLE_ROWS", self.user, f"Error displaying rows: {e}")

    # Insert row into table
    def insert_row(self, table_name, values_array):
        try:
            if self.cursor:
                placeholders = ",".join([":" + str(i+1) for i in range(len(values_array))])
                query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                self.cursor.execute(query, values_array)
                self.connection.commit()
                print('Row inserted successfully')
                createLog("INFO", "INSERT_ROW", self.user, "Row inserted successfully")
            else:
                print("Cursor not initialized")
                createLog("ERROR", "INSERT_ROW", self.user, "Cursor not initialized")
        except Exception as e:
            print(f"Error inserting row: {e}")
            createLog("ERROR", "INSERT_ROW", self.user, f"Error inserting row: {e}")

    # Delete record from table
    def delete_row(self, table_name, column_name, column_value):
        try:
            if self.cursor:
                self.cursor.execute(f"DELETE FROM {table_name} WHERE {column_name} = {column_value}")
                self.connection.commit()
                print('Row deleted successfully.')
                createLog("INFO", "DELETE_ROW", self.user, "Row deleted successfully")
            else:
                print("Cursor not initialized")
                createLog("ERROR", "INSERT_ROW", self.user, "Cursor not initialized")
        except Exception as e:
            print(f"Error inserting row: {e}")
            createLog("ERROR", "INSERT_ROW", self.user, f"Error inserting row: {e}")
