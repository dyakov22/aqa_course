import sqlite3


connection = sqlite3.connect('test.db')

cursor = connection.cursor()


# READ FROM DB
#
# result = cursor.execute('select * from users')
#
# result.fetchmany()

cursor.execute('update users set age = 10 where id == 1')

cursor.execute('update users set age = 10 where id == 1')

# connection.rollback()  #  Почистити пул коммітів

connection.commit()

connection.close()


