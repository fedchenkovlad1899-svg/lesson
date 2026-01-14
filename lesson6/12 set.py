n = int(input('введите максимальное число n: '))
st_avgust = set(range(1, n+1))
while len(st_avgust) > 3: #сделал отсеивание до 3возможнвх чисел т.к. нужно вывести несколько
    if len(st_avgust) <= 3:
        break
    second = input('введите множество и ответ(yes/no): ').split(' ')
    str_tris = second[0:-1]
    st_tris = set(list(map(int,str_tris)))
    answer = second[-1]
    ans = answer.lower()
    if ans == 'yes':
        st_avgust = st_tris
    if ans == 'no':
        st_avgust -= st_tris
    l_avg = list(st_avgust)
    l_avg.sort()
    print(l_avg)