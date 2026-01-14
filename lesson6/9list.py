lst = [5,2,0,-2,-7,1,8,0,-1]
lst_2 = []
lst_3 = []
lst_4 = []
for item in range(0,len(lst)):
    if int(lst[item]) > 0:
        lst_2.append(lst[item])
    if int(lst[item]) < 0:
        lst_3.append(lst[item])
    if int(lst[item]) == 0:
        lst_4.append(lst[item])
lst_2.extend(lst_3)
lst_2.extend(lst_4)
print(lst_2)