sample = input()

row1 = sample.split()

sum = 0
for i in range(4):
    sum += int(row1[i])

print(sum)