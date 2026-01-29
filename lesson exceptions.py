#1
try:
    x = (1, 2, 5, 7)
    x = x / 2
    print(x)
except TypeError as exc:
    print(exc.args)
except Exception as exc:
    print(exc.args)

#2
try:
    lst = [1,9,2]
    item = lst[4]
    print(item)
except IndexError:
    print('неверный индекс элемента')

#3
side_a = int(input('введите a: '))
side_b = int(input('введите b: '))
side_c = int(input('введите c: '))
semi_p = (side_a + side_b + side_c) / 2
s_abc =(semi_p * (semi_p - side_a) * (semi_p - side_b) * (semi_p - side_c)) ** 0.5
try:
    if side_a == 0 or side_b == 0 or side_c == 0:
        raise ArithmeticError
    else:
        print(s_abc)
except ArithmeticError :
    print('сторона не должна равняться 0')


#4
lst = list(input('введите список: ').split(' '))
num_del = input('элемент который надо удалить: ')
try:
    try:
        lst.remove(num_del)
        print(lst)
    except ValueError:
        raise TypeError
except TypeError:
    print('такого элемента в списке нет')

#5
dct = {'name':'ivan','surname':'sapogov','age':18,'city':'minsk'}
try:
    wrld = input('поиск по ключу: ')
    print(dct[wrld])
except KeyError as e:
    print('такого ключа нет')

#6
str = input('введите строку: ').split(' ')
sum = 0
for item in str:
    try:
        num = int(item)
        sum += num
    except ValueError:
        continue
print(sum)

#7
def string(txt):
    if not isinstance(txt, str):
        raise TypeError('error')
    for item in set(txt):
        if item == ' ':
            continue
        print(item,txt.count(item))
try:
    txt = 'aaa bb ss rra aa b'
    string(txt)
except TypeError  as e:
    print(f'нужен тип строка, {e}')
