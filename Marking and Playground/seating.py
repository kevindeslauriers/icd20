import random
import time
import os

students = [
    "Momeni, Arman", "Tai, Brandon", "Deng, Daniel", "Perry, David",
    "Anchekova, Eva", "He, Fred", "Cazzin, Harrison", "Kurian, James",
    "Chu, Kaiyan", "Carty, Kathryn", "Gao, Lester", "Mamdani, Rayhan",
    "Tran, Richie", "Glowczewski, Vanessa", "St-Onge, Vanessa", "Rodovinsky, Veronica"
]

# Shuffle the students list randomly
random.shuffle(students)

# Create a tuple with a number from 1 to 16 preceding each student's name
random_ordered_tuple = tuple(f"{i + 1}. {student}" for i, student in enumerate(students))

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Display the result with a delay of 5 seconds between each student
for student in random_ordered_tuple:
    print(student)
    time.sleep(10)
