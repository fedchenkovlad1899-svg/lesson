#1
def minimal (a,b):
    if a < b:
        mini = a
    else:
        mini = b
    return mini

x_1,x_2,x_3,x_4 = 9,2,3,5
print(minimal(minimal(x_1,x_2),minimal(x_3,x_4)))


#2
n = int(input('введите n: '))
def perfect_number(n):
    summa = 0
    for item in range(1,n):
        if n % item ==0:
            summa += item
    if summa == n:
        return True
if perfect_number(n):
    print('совершенное число')
else:
    print('не совершенное')


#3
n = int(input('введите n: '))
def fib(n):
    a,b = 0,1
    for item in range(n):
        a,b = b,a+b
    return a
print(fib(n))


#4
x = int(input('введите n: '))
def closest_mod_5(x):
    if x % 5 == 0:
        y = x
        return y
    else:
        y = x + (5 - (x % 5))
        return y
print(closest_mod_5(x))



#5


def check_variable(v):
    chars = '!@#$%^&*()'
    numbers = '0123456789'
    if v[0] in numbers:
        return False
    for item in range(len(v)):
        if v[item] in chars:
            return False
    return True
while True:
    v = input('введите строку: ')
    if v == 'поработали, и хватит':
        break
    if check_variable(v) :
            print('Можно использовать')
    else:
            print('Нельзя использовать')

#6
numbers = [i for i in range(10, 100) if i % 2 != 0]
print(numbers)

#7
numbers = [i for i in range(100, 1000) if i % 5 == 0 and i % 3 == 0]
print(numbers)


#8

lst = list(input('введите элементы списка: ').split(','))
lst.sort()
def counter(lst):
    count = 1
    for item in range(1,len(lst)):
        if lst[item-1] != lst[item]:
            count += 1
    return count
print(lst, counter(lst))


#9
lst = list(map(int, input('введите числа: ').split()))
def sum_neighb_elements(lst):
    lst_sum = []
    sum_n = 0
    for index in range(len(lst)):
        if len(lst) == 1:
            sum_n = lst[0]
            lst_sum.append(sum_n)
            break
        if index == 0:
            sum_n = lst[1] + lst[-1]
            lst_sum.append(sum_n)
        elif index == len(lst)-1:
            sum_n = lst[-2] + lst[0]
            lst_sum.append(sum_n)
        else:
            sum_n = lst[index - 1] + lst[index + 1]
            lst_sum.append(sum_n)
    return lst_sum
print(*sum_neighb_elements(lst))
