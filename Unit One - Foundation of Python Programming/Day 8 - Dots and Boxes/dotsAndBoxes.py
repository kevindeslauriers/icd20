# Initialize variables to store player's information
player_name = input("Enter your name: ")

# Game 1
print("Game #1:")
opponent1_name = input("Opponent's Name: ")
your_points1 = int(input("Your Points: "))
opponent1_points = int(input("Opponent's Points: "))
percentage_boxes_created1 = (your_points1 / 36) * 100

# Game 2
print("\nGame #2:")
opponent2_name = input("Opponent's Name: ")
your_points2 = int(input("Your Points: "))
opponent2_points = int(input("Opponent's Points: "))
percentage_boxes_created2 = (your_points2 / 36) * 100

# Game 3
print("\nGame #3:")
opponent3_name = input("Opponent's Name: ")
your_points3 = int(input("Your Points: "))
opponent3_points = int(input("Opponent's Points: "))
percentage_boxes_created3 = (your_points3 / 36) * 100

# Game 4
print("\nGame #4:")
opponent4_name = input("Opponent's Name: ")
your_points4 = int(input("Your Points: "))
opponent4_points = int(input("Opponent's Points: "))
percentage_boxes_created4 = (your_points4 / 36) * 100

# Game 5
print("\nGame #5:")
opponent5_name = input("Opponent's Name: ")
your_points5 = int(input("Your Points: "))
opponent5_points = int(input("Opponent's Points: "))
percentage_boxes_created5 = (your_points5 / 36) * 100

# Calculate the summary data
total_points = your_points1 + your_points2 + your_points3 + your_points4 + your_points5
total_opponent_points = opponent1_points + opponent2_points + opponent3_points + opponent4_points + opponent5_points
percentage_points_received = (total_points / (total_points + total_opponent_points)) * 100

# Print the table header
print("\nDots and Boxes Score Tracker\n")
print(f"Player's Name: {player_name}\n")
print("{:<20} {:<13} {:<18} {:<12}".format("Opponent", "Your Points", "Opponent Points", "Box %"))
print("=" * 63)

# Print game data for each game
print("{:<20} {:<13} {:<18} {:<12.2f}".format(opponent1_name, your_points1, opponent1_points, percentage_boxes_created1))
print("{:<20} {:<13} {:<18} {:<12.2f}".format(opponent2_name, your_points2, opponent2_points, percentage_boxes_created2))
print("{:<20} {:<13} {:<18} {:<12.2f}".format(opponent3_name, your_points3, opponent3_points, percentage_boxes_created3))
print("{:<20} {:<13} {:<18} {:<12.2f}".format(opponent4_name, your_points4, opponent4_points, percentage_boxes_created4))
print("{:<20} {:<13} {:<18} {:<12.2f}".format(opponent5_name, your_points5, opponent5_points, percentage_boxes_created5))

# Print summary data
print("=" * 63)
print("Summary:")
print(f"Total Points: {total_points}")
print(f"Total Opponent Points: {total_opponent_points}")
print("Percentage Points Received: {:.2f}%".format(percentage_points_received))
