import sqlite3

connection = sqlite3.connect('aqa_course_with_fk.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    email TEXT UNIQUE
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS user_details (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    address TEXT,
                    phone TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )''')

connection.commit()


cursor.execute('INSERT INTO users (name, age, email) VALUES ("name1", 100, "asssd@example.com")')

user_id = cursor.lastrowid

cursor.execute(f'INSERT INTO user_details (user_id, address, phone) VALUES ({user_id}, "address1", "3908312")')

cursor.connection.commit()

# connection.commit()

connection.close()