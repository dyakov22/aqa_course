import sqlite3

connection = sqlite3.connect('testing_data.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')


connection.commit()


for i in range(10):
    cursor.execute(f'INSERT INTO users (username, password) VALUES ("user{i}", "password{i}")')


cursor.connection.commit()

# connection.commit()

connection.close()
