school = {'9а':21,'9б':20,'9в':25,'9г':18,'9д':19}
school['9а'] = 22
school.update({'9e':17})
school.pop('9г')
print(sum(school.values()))
print(school)