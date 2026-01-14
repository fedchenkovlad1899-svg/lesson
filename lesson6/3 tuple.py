def natur(n):
    if n <= 1:
        return False
    for item in range(2,(int(n ** (1/2))+1)):
        if n % item == 0 and n != 2:
            return False
    return True
tup = (5,2,-2,7,-8,-9,1,7,9,11,22,4,13,23,17)
print("Простые числа:")
for i in  tup:
    if natur(i):
        print(i,end=" ")