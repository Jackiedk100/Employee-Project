first_names

with open('employees.txt', encoding='utf-8') as file:
    for line in file:
        data = line.split("\t")
        