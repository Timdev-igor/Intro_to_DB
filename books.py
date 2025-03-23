    #HAS CREATION OF DATABASES  CONNECTING TO SERVER  // CREATION OF TABLES,INSERTION OF DATA,DELETION AND SEARCHING
import mysql.connector

conn= mysql.connector.connect( 
    host="localhost",
    user="root",
    password="17999nf$xxjw23#$%&" 
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS library")
print("database created")

cursor.execute("USE library")
print("using database")

cursor.execute("""CREATE TABLE IF NOT EXISTS books(
               id INT AUTO_INCREMENT PRIMARY KEY,
               Title VARCHAR(255) NOT NULL,
               author VARCHAR(255) NOT NULL,
               ISBN VARCHAR(255) NOT NULL UNIQUE                  
               )
               """)
print("table created")

#MULTIPLE INSERTIONS
books_to_insert = [
    ("Death Stranding", "Hideo Kojima", "DEF45"),
    ("Daemon", "Hideo Kojima", "DEF44"),
    ("Doginn", "Markus", "DEF46"),
    ("The Silent Patient", "Alex Michaelides", "DEF47"),
    ("Sapiens", "Yuval Noah Harari", "DEF48"),
    ("The Hobbit", "J.R.R. Tolkien", "DEF49")
]

# Use executemany() for batch insertion
cursor.executemany("INSERT IGNORE INTO books (Title, Author, ISBN) VALUES (%s, %s, %s)", books_to_insert)
conn.commit()

print(f"✅ {cursor.rowcount} books inserted successfully!")

#search using a WHERE CONDITION

title = input("Enter book title to search: ").strip()   #STRIP REMOVES UNWANTED SPACING

query = "SELECT * FROM books WHERE Title LIKE %s"
cursor.execute(query, (f"%{title}%",))

results = cursor.fetchall()

print("\nBooks Table Content:")
print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'ISBN':<15}")
print("-" * 50)


for book in results:
    print(f"{book[0]:<5}   {book[1]:<30}   {book[2]:<20}   {book[3]:<15}")

# Close connection



cursor.execute("SELECT *FROM books ORDER BY ISBN ASC")
books = cursor.fetchall()

print("\nBooks Table Content:")
print(f"{'ID':<5} {'Title':<30} {'Author':<20} {'ISBN':<15}")
print("-" * 50)


for book in books:
    print(f"{book[0]:<5}   {book[1]:<30}   {book[2]:<20}   {book[3]:<15}")


delete_title = input("\n🗑️ Enter book title to delete: ").strip()#deletion

query = "DELETE FROM books WHERE Title LIKE %s"
cursor.execute(query, (f"%{delete_title}%",))
conn.commit()

if cursor.rowcount > 0:
    print(f"✅ '{delete_title}' deleted from the database.")
else:
    print(f"❌ No book found with the title '{delete_title}'.")



cursor.close()
conn.close()