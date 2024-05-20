The provided Python script implements a simple weather forecast system. It allows users to view weather forecasts for different locations by loading weather data from a file named `weather.data`. If this file does not exist, the script creates it with default weather data for a few predefined locations. The core functionality of the script includes loading and saving weather data, displaying weather forecasts for user-specified locations, and a basic user interface for interaction.

The script starts by importing necessary modules: `os` for operating system interactions and `pickle` for object serialization and deserialization. These imports are crucial for file operations and data persistence.

```python
import os
import pickle
```

The `clear_screen()` function enhances user experience by clearing the console screen before displaying new information. It uses the `os.system()` command to execute the appropriate command based on the operating system.

```python
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
```

The `display_title(title)` function is used to print a formatted title on the console, making the output more organized and user-friendly.

The `load_weather(filename)` function attempts to load existing weather data from the specified file. If the file is not found, it creates a new one with default weather data for New York, Los Angeles, and Chicago. This ensures the program can function even when starting for the first time or when the data file is missing.

```python
def load_weather(filename):
    # Attempts to load weather data or creates default data if file not found
```

The `save_weather(weather, filename)` function serializes and saves the current state of weather data to the specified file. This is essential for data persistence, allowing the program to maintain updated weather information across sessions.

The `display_weather(weather, location)` function checks if the specified location exists within the loaded weather data. If found, it displays the forecasted temperature, humidity, and conditions for that location. This function is key to providing the user with the requested weather forecast.

Finally, the `main()` function serves as the entry point of the program. It displays the program title, loads weather data (creating it with default values if necessary), and enters a menu loop allowing users to view weather forecasts for specific locations or exit the program. This loop facilitates user interaction with the system through a simple text-based menu.

```python
def main():
    # Main program flow: display title, load data, and menu loop for user interaction
```

The script concludes with a conditional statement that checks if it is being run directly. If so, it calls the `main()` function, initiating the program's execution.

This Python script demonstrates practical applications of file operations, data serialization with `pickle`, and basic user interface design in a console application.