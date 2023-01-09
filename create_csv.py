def creating ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Телефон;Описание\n')


# <!-- import csv

# with open("classmates.csv", encoding='utf-8') as r_file:
# file_reader = csv.reader(r_file, delimiter=",")
# for row in file_reader:
# print(row)

# with open("classmates1.csv", mode="w", encoding='utf-8') as w_file:
# file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
# row = ['Фамилия', 'Имя', 'Телефон']
# row1 = ['Иванов', 'Иван', '8876987']
# file_writer.writerow(row)
# file_writer.writerow(row1) -->