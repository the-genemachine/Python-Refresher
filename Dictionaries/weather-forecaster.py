""" This program provides a simple weather forecast system where users can view weather forecasts for different
locations. It loads weather data from the "weather.data" file (or creates it with default data if it doesn't exist),
allows users to input a location to view its weather forecast, and then displays the forecasted temperature,
humidity, and conditions for that location."""

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


# Function to load weather data from file
def load_weather(filename):
    try:
        with open(filename, 'rb') as file:
            weather = pickle.load(file)
    except FileNotFoundError:
        print("Weather data file not found. Creating a new one with default data.")
        weather = {
            "New York": {"temperature": 72, "humidity": 50, "conditions": "Sunny"},
            "Los Angeles": {"temperature": 80, "humidity": 60, "conditions": "Partly Cloudy"},
            "Chicago": {"temperature": 65, "humidity": 55, "conditions": "Rainy"}
        }
        save_weather(weather, filename)
    return weather


# Function to save weather data to file
def save_weather(weather, filename):
    with open(filename, 'wb') as file:
        pickle.dump(weather, file)


# Function to display weather forecast for a location
def display_weather(weather, location):
    if location in weather:
        print(f"Weather Forecast for {location}:")
        print(f"Temperature: {weather[location]['temperature']} F")
        print(f"Humidity: {weather[location]['humidity']}%")
        print(f"Conditions: {weather[location]['conditions']}")
    else:
        print("Location not found.")


# Main function
def main():
    # Title
    title = "Weather Forecast"
    display_title(title)

    # Load weather data from file or create new file with default data
    filename = "weather.data"
    weather = load_weather(filename)

    # Menu loop
    while True:
        print("\nMenu:")
        print("1. View weather forecast for a location")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            location = input("Enter location: ")
            display_weather(weather, location)
        elif choice == '2':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")


# Execute the main function
if __name__ == "__main__":
    main()
