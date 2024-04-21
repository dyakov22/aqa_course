'''
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'''

import os

file_path = os.path.dirname(__file__) + '/text.txt'

# file = open(file_path, mode='w' if not os.path.exists(file_path) else 'a')

# print(file.readable())
# print(file.writable())
# print(file.readlines())  'r'


# file.writelines(['hello', 'hello2'])
# file.write('hello\n')
# file.write('hello1')


# file.close()


# class N:
#     def __enter__(self):
#         pass
#
# __exit__

result = range(100)

with open(name=file_path, mode='w' if not os.path.exists(file_path) else 'a') as file:
    print(file.mode)
    print(file.name)
