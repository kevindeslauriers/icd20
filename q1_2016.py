lines = int(input())
dict = {"Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 12500}
score = 0
for i in range(lines):
    name = input()
    score += int(dict[name])
print(score)