import os

file_name = input('Введите путь к файлу: ')
if not os.path.isfile(file_name):
    exit('Файл не существует')
if os.path.splitext(file_name)[-1] != '.txt':
    exit('Файл должен иметь формат txt')
print('Очереди')
with open(file_name, encoding='utf-8') as numbers_file:
    numbers = numbers_file.readlines()
queues = []
for line in numbers:
    line = line.strip()
    if not line:
        continue
    number = [x.strip() for x in line.split(',') if x.strip()]
    print(', '.join([x for x in number]))
    queues += [number]
if not queues:
    exit('Введён пустой файл')
numbers = []
for i in range(max([len(x) for x in queues])):
    for j in range(len(queues)):
        try:
            numbers += [queues[j][i]]
        except IndexError:
            continue
print('Ответ:')
print(', '.join([x for x in numbers]))
