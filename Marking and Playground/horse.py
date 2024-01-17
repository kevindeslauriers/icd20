import csv
from faker import Faker

fake = Faker()

# Common horse race distances in furlongs
race_distances = [5, 5.5, 6, 7, 8, 9, 10, 12]

# Create a list to store horse data
horse_data = []

# Generate data for 10 fake horses with funny names
for _ in range(150):
    horse_name = fake.word().capitalize() + " " + fake.word().capitalize()
    mud_rating = fake.random_int(min=1, max=10)
    grass_rating = fake.random_int(min=1, max=10)
    dirt_rating = fake.random_int(min=1, max=10)
    
    # Select a random race distance in furlongs for the preferred length
    preferred_length = fake.random_element(elements=race_distances)

    # Append horse data to the list
    horse_data.append([horse_name, mud_rating, grass_rating, dirt_rating, preferred_length])

# Write the data to a CSV file
csv_file_path = "funny_horse_data.csv"
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Name", "Mud Rating", "Grass Rating", "Dirt Rating", "Preferred Length"])

    # Write horse data
    writer.writerows(horse_data)

print(f"CSV file created successfully: {csv_file_path}")
