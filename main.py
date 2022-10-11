import csv

# Загрузить данные из csv
data = []
with open('datasets/ads.csv', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        data.append(row)


# уникализируем авторов? запись в файл authors.csv
authors = []
for i in data:
    if i != data[0]:
        authors.append(i[2])
uniq_authors = set(authors)
count = 1
with open('authors.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for author in uniq_authors:
        writer.writerow([count,author])
        count += 1

# уникализируем адреса
adresses = []
for a in data:
    if a != data[0]:
        adresses.append(a[5])
uniq_adresses = set(adresses)
count = 1
with open('adresses.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for adress in uniq_adresses:
        writer.writerow([count,adress])
        count += 1

#создаем новый файл с заменой по значениям авторов и адресов
# new_data = []
# with open('new_data.csv', 'w', newline='', encoding='utf-8') as file_new:
#     writer = csv.writer(file_new)
#     for x in data:
#         if x != data[0]:
#             new_data.append([x[0],x[1],x[2],x[]])
#     writer.writerow([count,adress])
# for d in data:
#     if d[2] in authors.csv
adresses_file = []
with open('adresses.csv', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        adresses_file.append(row)

authors_file = []
with open('authors.csv', newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        authors_file.append(row)

with open('new_table.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for d in data[1:]:
        for author in authors_file:
            if d[2] == author[1]:
                d[2] = author[0]
        for adr in adresses_file:
            if d[5] == adr[1]:
                d[5] = adr[0]
        writer.writerow(d)



