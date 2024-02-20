from faker import Faker
import random

fake = Faker()

# Function to generate random baseball statistics for a player
def generate_random_baseball_stats():
    return {
        "Name": fake.name(),
        "Hits": random.randint(10, 500),
        "Runs": random.randint(5, 120),
        "RBIs": random.randint(5, 120),
    }

# Function to create a sample data file with realistic values for a full season
def create_sample_data_file(file_path, num_players):
    with open(file_path, "w") as file:
        # Write header
        file.write("Name,Hits,Runs,RBIs\n")

        # Write data for each player
        for _ in range(num_players):
            player_stats = generate_random_baseball_stats()
            file.write(f"{player_stats['Name']},{player_stats['Hits']},{player_stats['Runs']},{player_stats['RBIs']}\n")

# Main program
if __name__ == "__main__":
    # Specify the file path and the number of players
    file_path = "baseball_stats_generated.txt"
    num_players = 600  # Adjust the number of players as needed

    # Create a sample data file with realistic values
    create_sample_data_file(file_path, num_players)
