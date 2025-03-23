import mysql.connector

# First, connect to MySQL without selecting a database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="17999nf$xxjw23#$%&"  # Your MySQL root password
)

cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS testkit")
print("Database  created successfully!")

cursor.execute("USE testkit;")
print("Using database 'testkit'.")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    )
""")
print("Table 'users' is ready.")


sql="INSERT IGNORE INTO users (name,email) VALUES (%s, %s)"
val=("johny", "johnycage@gmail.com")
cursor.execute(sql, val)
conn.commit()

sql="INSERT IGNORE INTO users (name,email) VALUES (%s, %s)"
val=("johny", "johnycage@gmail.com")
cursor.execute(sql, val)
conn.commit()


# Close the initial connection
cursor.execute("SELECT * FROM users;")
users = cursor.fetchall()

# Display table contents
print("\nUsers Table Content:")
print("ID | Name  | Email")
print("-" * 30)

for user in users:
    print(f"{user[0]} | {user[1]} | {user[2]}")


conn.close()

