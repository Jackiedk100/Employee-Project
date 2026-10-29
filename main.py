first_names = [] #første kolonne
job_titles = [] #andre kolonne

with open('employees.txt', encoding='utf-8') as file:
    for line in file:
        data = line.strip().split("\t")
        first_names.append(data[0])
        job_titles.append(data[2])

for name, title in zip(first_names, job_titles):
    print(name+":", title)