import psycopg2

connection = psycopg2.connect(
    host='localhost',
    port=5432,
    database='testdb',
    user='testuser',
    password='testpassword'
)

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         id SERIAL PRIMARY KEY,
#                         name VARCHAR(100) NOT NULL,
#                         age INTEGER,
#                         email VARCHAR(100) UNIQUE
#                     )''')
#
# connection.commit()

# cursor.execute('''INSERT INTO users (name, age, email) VALUES ('HELLASDQW', 12, 'asd@asd.asd')''')

# connection.commit()

users = [
    ('name1', 10, 'asd@asd2123.com'),
    ('name11', 110, 'asd@asd21223.com'),
    ('name12', 120, 'a1sd@asd2123.com')
]


cursor.executemany('''INSERT INTO users (name, age, email) VALUES (%s, %s, %s)''', users)

connection.commit()







cursor.close()
connection.close()