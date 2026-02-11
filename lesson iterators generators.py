'''

1.	Создайте класс RangeIterator, который реализует протокол итератора (__iter__, __next__).
Итератор должен возвращать числа в заданном диапазоне с указанным шагом. После окончания итерации
должно выбрасываться исключение StopIteration
'''
class RangeIterator:
    def __init__(self, min_num:int, max_mun:int,step:int):
        self.min_num = min_num
        self.max_mun = max_mun
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.min_num >= self.max_mun:

            raise StopIteration
        number = self.min_num
        self.min_num += self.step
        return number

iterator = RangeIterator(1,10,4)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


'''2.Напишите генераторную функцию fibonacci(limit),которая возвращает последовательность Фибоначчи
 до заданного предела. Генерация должна останавливаться, когда значение превышает limit.
'''
def fibonachi(limit):
    a,b = 0,1
    while a <= limit:
        yield a
        a,b = b,a+b
fib = fibonachi(10)
for elem in fib:
    print(elem)

'''
3.Создайте класс LogReader, который читает строки из источника данных и является итерируемым объектом.
Класс должен:
-	поддерживать перебор через for
-	пропускать пустые строки
-	возвращать строки по одной без загрузки всех данных в память
'''



'''
4.	Напишите генераторную функцию flatten(iterable),
которая принимает вложенную структуру (списки внутри списков) и возвращает элементы в плоском виде.
Решение должно корректно обрабатывать любую глубину вложенности.

'''
def flatten(iterable):
    while iterable:
        last_elem = iterable.pop()
        if isinstance(last_elem, list):
            iterable.extend(reversed(last_elem))
        else:
            yield last_elem
flat = flatten([[1, [2, 3], [[4], 5], 6]])
for item in flat:
    print(item,end = ' ')


