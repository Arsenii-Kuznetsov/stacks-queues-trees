import os
from re import findall

file_name = input('Введите путь к файлу: ')
if not os.path.isfile(file_name):
    exit('Файл не существует')
if os.path.splitext(file_name)[-1] != '.txt':
    exit('Файл должен иметь формат txt')
with open(file_name, encoding='utf-8') as numbers_file:
    numbers = []
    while True:
        line = numbers_file.readline()
        if not line:
            break
        line = line.strip()
        if line:
            numbers += [x for x in findall('[А-Я][1-9][0-9]*', line)]
numbers.sort(key=lambda x: (x[0],int(x[1:])))
queues = []
added = []
for number in numbers:
    if number[0] in added:
        continue
    numbers_list = [x for x in numbers if x[0] == number[0]]
    print(', '.join([x for x in numbers_list]))
    queues += [numbers_list]
    added += [number[0]]
if not queues:
    exit('В файле не найдено подходящих номеров')
numbers = []
max_len = max(max([len(x) for x in queues]), len(queues))
for i in range(max_len):
    for j in range(len(queues)):
        try:
            numbers += [queues[j][i]]
        except IndexError:
            continue
print('Ответ')
print(', '.join([x for x in numbers]))
