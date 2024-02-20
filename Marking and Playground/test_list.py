sum = 0

if list[0] != 13:
    sum += list[0]
for i in range(1, len(list)):
    if list[i] != 13 and list[i-1] != 13:
        sum += list[i]  



