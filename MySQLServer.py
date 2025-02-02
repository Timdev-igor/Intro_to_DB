import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="17999nf$xxjw23#$%&")
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")

cursor.close()
connection.close()

