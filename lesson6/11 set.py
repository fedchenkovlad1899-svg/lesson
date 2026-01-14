st_lst = input('Введите список положительных целых чисел: ').split(' ')
#print(type(st_lst))
st_set = set()
for item in st_lst:
    if item not in st_set:
        print('no')
        st_set.add(item)
    else:
        print('yes')