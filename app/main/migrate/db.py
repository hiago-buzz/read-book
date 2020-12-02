import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute('CREATE TABLE books (id integer primary key autoincrement, title TEXT, author TEXT, genre TEXT, finish DATE, createAt DATETIME)')
print("Table created successfully");
conn.close()