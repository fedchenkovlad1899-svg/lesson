lst = input('Введите список положительных целых чисел: ')
lst_list = list(map(int,lst.split(' ')))
lst_2 = []
def perevert(lst_list):
    return int(str(lst_list)[::-1])
for item in range(0,len(lst_list)):
    if int(lst_list[item]) % 2 == 0:
        lst_2.append(lst_list[item])
        lst_2.append(perevert(lst_list[item]))
    else:
        lst_2.append(lst_list[item])
print(lst_2)



