dct = {}

while True:
    line = input('заполните словарь: ')
    if line == '.':
        break
    pon, opred = line.split('-')
    dct[pon] = opred
m = int(input('количество запросов: '))

for item in range(m):
    pon_2 = input('слэнг-слово: ')
    if pon_2 in dct:
        print(dct[pon_2])
    else:
        print('не определено')