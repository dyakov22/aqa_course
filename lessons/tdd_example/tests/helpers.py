import csv


def read():
    with open('login_data.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        login_data = []
        for row in reader:
            login_data.append(row)
        return login_data
