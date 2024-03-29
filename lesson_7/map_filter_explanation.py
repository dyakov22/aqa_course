import csv


def is_number(item):
    if isinstance(item, int):
        return item
    else:
        return False


l = [1, 2, 3, 4, 5]


def filter_1(func, iterable):
    for item in iterable:
        if func(item):
            yield item


import os

# variant 1

currency_rate = 39


dir_path = os.path.dirname(__file__)
file_path = os.path.join(dir_path, 'salaries_uah.csv')

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(__file__)
    users_salaries = list(csv_reader)
    months = users_salaries[0]
    salaries_uah = []
for row in users_salaries[1:]:
    employee = row[0]
    salaries = [int(salary) * currency_rate for salary in row[1:]]
    salaries.insert(0, employee)
    salaries_uah.append(salaries)
with open('salaries_uah.csv', mode='w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(months)
    csv_writer.writerows(salaries_uah)


# variant 2


currency_rate = 39


dir_path = os.path.dirname(__file__)
file_path = dir_path + '/salaries_uah.csv'

with open(dir_path + '/salaries_uah.csv', mode='r') as file:
    csv_reader = csv.reader(__file__)
    users_salaries = list(csv_reader)
    months = users_salaries[0]
    salaries_uah = []
for row in users_salaries[1:]:
    employee = row[0]
    salaries = [int(salary) * currency_rate for salary in row[1:]]
    salaries.insert(0, employee)
    salaries_uah.append(salaries)
with open('salaries_uah.csv', mode='w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(months)
    csv_writer.writerows(salaries_uah)


