""" This program allows users to track scores and statistics for players in a game. It loads player data from the
"scores.data" file (or creates it with default data if it doesn't exist), provides options to view player details,
update player scores, and add achievements, and then saves the updated player data back to the file. Each player is
associated with a unique player ID, and their details are stored in a dictionary."""

import os
import pickle


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display a title
def display_title(title):
    clear_screen()
    print("=" * len(title))
    print(title)
    print("=" * len(title))
    print()


# Function to load player data from file
def load_players(filename):
    try:
        with open(filename, 'rb') as file:
            players = pickle.load(file)
    except FileNotFoundError:
        print("Player data file not found. Creating a new one with default data.")
        players = {
            "1": {"name": "Player 1", "score": 100, "achievements": ["Level 1 Completed"]},
            "2": {"name": "Player 2", "score": 150, "achievements": ["Level 2 Completed"]},
            "3": {"name": "Player 3", "score": 200, "achievements": ["Level 3 Completed"]}
        }
        save_players(players, filename)
    return players


# Function to save player data to file
def save_players(players, filename):
    with open(filename, 'wb') as file:
        pickle.dump(players, file)


# Function to display player details
def display_player_details(players, player_id):
    if player_id in players:
        print(f"Player ID: {player_id}")
        print(f"Name: {players[player_id]['name']}")
        print(f"Score: {players[player_id]['score']}")
        print("Achievements:")
        for achievement in players[player_id]['achievements']:
            print(f"- {achievement}")
    else:
        print("Player not found.")


# Function to update player score
def update_player_score(players, player_id, score):
    if player_id in players:
        players[player_id]['score'] = score
        print("Score updated successfully.")
    else:
        print("Player not found.")


# Function to add achievement for player
def add_achievement(players, player_id, achievement):
    if player_id in players:
        players[player_id]['achievements'].append(achievement)
        print("Achievement added successfully.")
    else:
        print("Player not found.")


# Main function
def main():
    # Title
    title = "Player Statistics Tracker"
    display_title(title)

    # Load player data from file or create new file with default data
    filename = "scores.data"
    players = load_players(filename)

    # Menu loop
    while True:
        print("\nMenu:")
        print("1. View player details")
        print("2. Update player score")
        print("3. Add achievement for player")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            player_id = input("Enter player ID: ")
            display_player_details(players, player_id)
        elif choice == '2':
            player_id = input("Enter player ID: ")
            score = int(input("Enter new score: "))
            update_player_score(players, player_id, score)
        elif choice == '3':
            player_id = input("Enter player ID: ")
            achievement = input("Enter achievement: ")
            add_achievement(players, player_id, achievement)
        elif choice == '4':
            save_players(players, filename)
            print("Player data saved. Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Execute the main function
if __name__ == "__main__":
    main()
