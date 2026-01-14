tup = (5,2,-2,7,-8,-9,1)
cnt = 0
for item in range(1,len(tup)):
    if tup[item-1] * tup[item] < 0:
        cnt += 1
    else:
        cnt == 0
print(cnt)