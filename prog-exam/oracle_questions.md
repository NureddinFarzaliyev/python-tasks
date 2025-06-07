### 35

```python
import oracledb

connection = oracledb.connect(
	user="username",
	password="1234",
	dsn="localhost/xe"
)

cursor = connection.cursor()

cursor.execute("SELECT first_name, last_name FROM employees")

while True:
	row = cursor.fetchone()
	if row is None:
		break
	print(f"The name of the employee is {row[0]} {row[1]}")

cursor.close()
connection.close()
```

### 36

```python
import oracledb

connection = oracledb.connect(
	user="testuser",
	password="123456",
	dsn="localhost/xe"
)

cursor = connection.cursor()

cursor.execute("SELECT username, points FROM users")

while True:
	rows = cursor.fetchmany(100)
	if not rows:
		break;
	for row in rows:
		print(f"User {row[0]} has {row[1]} points!")

cursor.close()
connection.close()
```

```python
import oracledb

connection = oracledb.connect(
	user="testuser",
	password="123456",
	dsn="localhost/xe"
)

cursor = connection.cursor()

cursor.execute("SELECT username, points FROM users")

def fetch_page(limit):
	return cursor.fetchmany(limit)

while True:
	choice = input("<enter> - next page \n <q+enter> - quit ").lower()
	if choice == "q":
		break
	else:
		rows = fetch_page(10)
		if not rows:
			print("No more pages")
		else:
			for row in rows:
				print(f"User {row[0]} has {row[1]}pts.")
```

### 37

```python
import oracledb

connection = oracledb.connect(
	user="testuser",
	password="123456",
	dsn="localhost/xe"
)

cursor = connection.cursor()

cursor.execute("""
	CREATE TABLE departments(
		D_ID NUMBER PRIMARY_KEY,
		D_Name, VARCHAR2(100) NOT NULL,
		D_Address, VARCHAR2(100) NOT NULL,
	)
""")

data = [
    (1, 'HR', 'Building A'),
    (2, 'IT', 'Building B'),
    (3, 'Finance', 'Building C')
]

cursor.executemany("""INSERT INTO
	departments (D_ID, D_Name, D_Address)
	VALUES (:1 :2 :3)
""", data)

connection.commit()
```

### 41

```python
import requests
import oracledb

response = requests.get("https://exampleurl.com/users")
users = response.json()

connection = oracledb.connect(
	user="testuser",
	password="123456",
	dsn="localhost/xe"
)

cursor = connection.cursor()

cursor.execute("""
	CREATE TABLE users (
		id NUMBER PRIMARY KEY,
		username VARCHAR2(100),
		email VARCHAR2(100)
	)
""")

for user in users:
	cursor.execute(
		"""INSERT INTO
			users (id, username, email)
			VALUES (:1 :2 :3)""",
		(user["id"], user["username"], user["email"])
	)

connection.commit()
cursor.close()
connection.close()
```

### 43

```python
import oracledb

connection = oracledb.connect(
    user="testuser",
    password="123456",
    dsn="localhost/xe",
)

cursor = connection.cursor()

# Change the last name of the user whose id is 3
def update_name_by_id(id, name):
    cursor.execute("UPDATE users SET name = :2 WHERE id = :1", (id, name))
    print(f"Name of the user with id {id} successfully updated to {name}")


update_name_by_id(2, "Alice")
update_name_by_id(4, "John")

connection.commit()

cursor.close()
connection.close()
```
