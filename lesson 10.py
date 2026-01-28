#1 Написать декоратор log_result, который печатает результат выполнения функции. Применить к функции возведения числа в квадрат.

def log_result(func):
    def wrapper(n):
        new = func(n)
        print(f'число в квадрате: {new}')
        return new
    return wrapper
@log_result
def my_function(n):
    return n ** 2
num = int(input('введите число: '))
my_function(num)


#2 Написать декоратор repeat(n), который повторяет вызов функции n раз и возвращает последний результат

n_v = int(input('вваедите n: '))
def repeat(n:int):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            a = None
            for item in range(n):
                a = func(*args, **kwargs)
            return a
        return wrapper
    return my_decorator
@repeat(n_v)
def my_func():
    str_a = 'пу-пу-пу'
    print(str_a)
    return f'помследний результат: {str_a}'

print(my_func())



#3 Написать декоратор bench, который измеряет ошибки: если функция завершилась ошибкой, вывести её тип и сообщение.

a:int = 5
b = [1,2,3]
def bench(func):
    def inner(a,b):
        try:
            item = func(a,b)
            return item
        except TypeError as e:
            return f'тип ошибки: {type(e).__name__} при сложении: {" и ".join(map(str, e.args))}'
    return inner
@bench
def some_function(a,b):
    if type (b) == list:
        raise TypeError(a,b)
    return a + b
print(some_function(5,3))
print(some_function(a,b))



#4 Дан список слов. Получить список их длин.

lst = ['apple', 'Banana', 'cherry', 'DATE','']
new_lst =[len(el) for el in lst]
print(new_lst)

#5 Дан список: ['apple', 'Banana', 'cherry', 'DATE']. Получите новый список, оставив только слова в нижнем регистре.

lst = ['apple', 'Banana', 'cherry', 'DATE']
new_lst = [el for el in lst if  el.islower()]
print(new_lst)


#6 Дан список кортежей (имя, возраст). Получите новый список, оставив кортеж в котором возраст > 18.

lst = [('ваня',22),('оля',15),('лена',19)]
new_lst = [(name,age) for name,age in lst if age>18 ]
print(new_lst)


#7 Дан список списков: [[1,2],[3,4],[5,6]]. С помощью reduce объединить в один список: [1,2,3,4,5,6].

from functools import reduce
lst = [[1,2],[3,4],[5,6]]
new_lst = reduce(lambda x,y : x + y,lst)
print(new_lst)


#8 Дан список ['cat','car','mouse','dog','snake','cow'].Получить словарь: {начальная буква: [слова...]}.


lst = ['cat','car','mouse','dog','snake','cow']
dct = {e[0]: [el for el in lst if el[0]==e[0]] for e in lst}
print(dct)


#9 	Дан список кортежей (товар, цена, количество).Получить список сумм: цена * количество.

lst = [('Яблоко',14.25,5),('Рыба',18.2,9),('Молоко',3.15,2),('Стейк',111.2,3)]
sum_lst = list(map(lambda x: x[1]*x[2], lst))
print(sum_lst)

