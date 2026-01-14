lst_1 = [4,1,6,9]
lst_2 = [8,1,2,4,9,5,7,6]
lst_3 = []
result = list(set(lst_1) - set(lst_2))
if result == []:
    print('таких элементов нет')
else:
    for item in lst_1:
        if item not in lst_2:
            lst_3.append(item)
    print(min(lst_3))
