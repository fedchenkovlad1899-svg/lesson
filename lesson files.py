'''
1.	Создать текстовый файл и записать в него 6 строк. Записываемые строки вводятся с клавиатуры.
'''
import os
with open(file = 'D:\\my_file.txt',mode =  'w',encoding = 'utf-8') as file:
    print('введите 6 строк ')
    for item in range(6):
        line = input(f'строка {item+1}: ')
        file.write(line+'\n')

'''
2.	В конец существующего текстового файла записать три новые строки текста. Записываемые строки вводятся с клавиатуры.
'''
import os
with open(file = 'D:\\my_file.txt',mode =  'a',encoding = 'utf-8') as file:
    print('добавьте 3 строки ')
    for item in range(3):
        line = input(f'строка {item+1}: ')
        file.write(line+'\n')

'''
3.	Дан текстовый файл. Подсчитать количество символов в нем. Без \n
'''
import os
with open(file = 'D:\\my_file.txt',mode =  'r',encoding = 'utf-8') as file:
    data = file.read()
    count_char = data.replace('\n','')
    print(len(count_char))

'''
4.	Имеется текстовый файл, содержащий 5 строк. Переписать каждую из его строк в список в том же порядке. 
'''
import os
with open(file='D:\\1.txt',mode='r',encoding='utf-8') as file:
    lines=file.read().splitlines()
    print(lines)

'''
5.	Имеется текстовый файл. Получить текст, в котором в конце каждой строки из заданного файла
 добавлен восклицательный знак. 
'''
import os
with open(file='D:\\1.txt',mode='r',encoding='utf-8') as file:
    for lines in file:
        lines=lines.strip()
        if  lines and lines[-1]=='!':
            print(lines)


'''
6.	В справочной аэропорта хранится расписание вылета самолетов на следующие сутки.
Для каждого рейса указаны номер рейса, пункт назначения, время вылета.
Вывести все номера рейсов и время вылета самолета для заданного пункта назначения.
Пример файла flights.json

Simple Input:
Москва
Simple Output:
SU123 08:30
BT789 18:40
'''

import json
with open(file = 'D:\\flights.json',mode = 'r',encoding='Utf-8') as file:
    data = json.load(file)
    direction_fly = input('введите пункт назначения: ')
    correct_direction = None
    for item in data:
        if item['destination']== direction_fly:
            print(item['flight_number'],item["departure_time"])
            correct_direction = True
        else:
            correct_direction = False
    if correct_direction == False :
            print('нет такого пункта назначения')


'''
7.	Ведомость студентов, сдававших сессию, содержит ФИО и оценки по четырем предметам.
 Вывести список студентов, сдавших сессию со средним баллом больше 7.
 Пример файла student_grades.json
[
  {
    "full_name": "Иванов Иван",
    "grades": [8, 9, 7, 10]
  },
  {
    "full_name": "Петров Петр",
    "grades": [6, 7, 5, 8]
  },
  {
    "full_name": "Сидорова Анна",
    "grades": [9, 8, 9, 9]
  }
]
Simple Output:
Иванов Иван — средний балл: 8.5
Сидорова Анна — средний балл: 8.75
'''

import json
with open(file = 'D:\\student_grades.json',mode = 'r',encoding='Utf-8') as file:
    data = json.load(file)

    for item in data:
        average = sum(item['grades']) / len(item['grades'])
        if average>= 7:
            print(f'{item['full_name']} - средний балл: {average}')




