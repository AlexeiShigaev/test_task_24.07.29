import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )"""
)

new_data = [
    ("Иванов", 25),
    ("Петров", 32),
    ("Сидоров", 40),
    ("Кукушкин", 19)
]
cursor.executemany(
    "INSERT INTO Users (name, age) VALUES(?, ?)",
    new_data
)
connection.commit()

cursor.execute(
    "SELECT name, age FROM Users WHERE age > 30"
)
results = cursor.fetchall()
[print("name: {}\tage: {}".format(name, age)) for name, age in results]

connection.close()
