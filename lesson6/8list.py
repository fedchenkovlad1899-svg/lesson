lst = [5,2,4,5,1,2]
lst_2 = []
s_1 = ''
while lst:
    min_n = min(lst)
    lst_2.append(min_n)
    lst_2.count(min_n)
    lst.remove(min_n)
kol = 1
for item in range(1, len(lst_2)):
    if lst_2[item-1] == lst_2[item]:
        kol += 1
    else:
        s_1 += str(lst_2[item-1]) + ' - ' + str(kol) + ' '
        kol = 1
s_1 += str(lst_2[-1]) + ' - ' + str(kol)
print(s_1)