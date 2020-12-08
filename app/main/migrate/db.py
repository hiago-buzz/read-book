import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");

conn.execute("PRAGMA foreign_keys = on")
conn.execute('CREATE TABLE if not exists users (user_name TEXT primary key NOT NULL, full_name TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, createAt DATETIME)')

conn.execute('CREATE TABLE if not exists books (id integer primary key autoincrement, title TEXT NOT NULL, author TEXT, genre TEXT, finish DATE, createAt DATETIME NOT NULL, user_name TEXT, FOREIGN KEY(user_name) REFERENCES users(user_name) ON DELETE CASCADE)')
print("Table created successfully");
conn.close()