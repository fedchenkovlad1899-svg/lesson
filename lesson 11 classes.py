'''
1.Создать класс с двумя переменными. Добавить функцию вывода на экран и функцию изменения
этих переменных. Добавить функцию, которая находит сумму значений этих переменных,и функцию которая
находит наибольшее значение из этих двух переменных.
'''
class Numb():
    def __init__(self,num_1,num_2):
        self.num_1 = num_1
        self.num_2 = num_2
    def print_num(self):
        print(f'переменная num_1: {self.num_1},переменная num_2: {self.num_2}')
    def new_num(self,new_num_1,new_num_2):
        self.num_1 = new_num_1
        self.num_2 = new_num_2
    def sum_numb(self):
        return self.num_1 + self.num_2
    def max(self):

        if self.num_2 > self.num_1:
            return self.num_2
        else:
            return self.num_1

numbers = Numb(1,2)
numbers.print_num()
numbers.new_num(3,5)
print(f'измененные numb_1: {numbers.num_1}, numb_2: {numbers.num_2}')
print('сумма:',numbers.sum_numb())
print(f'максимальное число:' ,numbers.max())

'''
2.	Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение 
на единицу в заданном диапазоне. Предусмотреть инициализацию счетчика значениями по умолчанию и
 произвольными значениями. Счетчик имеет два метода: увеличения и уменьшения, — и свойство, 
 позволяющее получить его текущее состояние. Написать программу, демонстрирующую все возможности класса.
'''
class DecCounter():
    def __init__(self,current_c =0,min_c = 0,max_c = 10):
        self.current_c = current_c
        self.min_c = min_c
        self.max_c = max_c
    def get_current_c(self):
        return self.current_c

    def up_counter(self):
        if self.current_c >= self.max_c:
            raise Exception('Достигнуто максимальное значение счетчика')
        else:
            self.current_c < self.max_c
            self.current_c += 1

    def down_counter(self):

        if self.current_c <=self.min_c:
            raise Exception('Достигнкто минимальное значение счетчика')
        else:
            self.current_c > self.min_c
            self.current_c -= 1

try:
    count = DecCounter()
    count.up_counter()
    #count.down_counter() #что-то одно на выбор чтобы юолее понятен был результат вывода
    print(f'текущее значение счетчика: ',count.get_current_c())

except Exception as e:
    print(f'ошибка: ', *e.args)

