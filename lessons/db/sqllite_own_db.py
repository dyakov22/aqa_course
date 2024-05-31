import sqlite3

connection = sqlite3.connect('aqa_course.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER
                    )''')

connection.commit()

# mapping = [('name1', 10),
#            ('name2', 11),
#            ('name3', 12),
#            ('name4', 13),
#            ('name5', 14),
#            ('name6', 15),
#            ('name7', 16),
#            ('name5', 17),
#            ]
#
#
# for user in mapping:
#     cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', user)
#     connection.commit()


# result = cursor.execute('select * from users')
# print(result.fetchall())
#
result = cursor.execute('select * from users where name == "name2"')
print(result.fetchall())


delete_result = cursor.execute('delete from users where name == "name2"')

connection.commit()

result = cursor.execute('select * from users where name == "name2"')
print(result.fetchall())

