import json

"""
json.load()
json.loads()

json.dump()
json.dumps()
"""


""" LOAD """
# with open("../files_for_parsing/example.json", "r") as file:
#     data_from_file = json.load(file)
#     # print(data_from_file)
#     print(type(data_from_file))
#     print(data_from_file.get("library")[0].get("year"))


# {
#     'library': [{'type': 'book', 'id': '1', 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925,
#                  'publisher': 'Scribner'},
#                 {'type': 'book', 'id': '2', 'title': '1984', 'author': 'George Orwell', 'year': 1949,
#                  'publisher': 'Secker & Warburg'},
#                 {'type': 'book', 'id': '3', 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960,
#                  'publisher': 'J.B. Lippincott & Co.'},
#                 {'type': 'magazine', 'id': '1', 'title': 'National Geographic', 'issue': 'May 2024'},
#                 {'type': 'magazine', 'id': '2', 'title': 'Time', 'issue': 'June 2024'}]}

# ['{\n', '  "library": [\n', '    {\n', '      "type": "book",\n', '      "id": "1",\n',
#  '      "title": "The Great Gatsby",\n', '      "author": "F. Scott Fitzgerald",\n', '      "year": 1925,\n',
#  '      "publisher": "Scribner"\n', '    },\n', '    {\n', '      "type": "book",\n', '      "id": "2",\n',
#  '      "title": "1984",\n', '      "author": "George Orwell",\n', '      "year": 1949,\n',
#  '      "publisher": "Secker & Warburg"\n', '    },\n', '    {\n', '      "type": "book",\n', '      "id": "3",\n',
#  '      "title": "To Kill a Mockingbird",\n', '      "author": "Harper Lee",\n', '      "year": 1960,\n',
#  '      "publisher": "J.B. Lippincott & Co."\n', '    },\n', '    {\n', '      "type": "magazine",\n',
#  '      "id": "1",\n', '      "title": "National Geographic",\n', '      "issue": "May 2024"\n', '    },\n', '    {\n',
#  '      "type": "magazine",\n', '      "id": "2",\n', '      "title": "Time",\n', '      "issue": "June 2024"\n',
#  '    }\n', '  ]\n', '}\n']



""" LOADS """

# obj = '{"key1": "value1", "key2": "value2"}'
#
# data = json.loads(obj)
#
# print(data.get('key1'))



# obj = "{'key1': 'value1', 'key2': 'value2'}"
# print(type(eval(obj)))


""" DUMP """


json_to_write = {
      "type": "book",
      "id": "1",
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "year": 1925,
      "publisher": "Scribner"
    }


# with open('example1.json', 'w') as file:
#     json.dump(json_to_write, file)










