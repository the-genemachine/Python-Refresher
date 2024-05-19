"""Here's a Python program that analyzes a text document, counts the frequency of each word, and stores the results
in a dictionary. If the "words.data" file doesn't exist, the program creates it and populates it with a short story.
Then, it reads the story, tokenizes it into words, and calculates the frequency of each word using a dictionary."""

import os
import string
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


# Function to load text data from file
def load_text(filename):
    """
    Load text data from a specified file or create a new file with default text if not found.

    This function attempts to open a file with the given filename to read text data. If the file does not exist,
    indicated by a FileNotFoundError, the function creates a new file with a default text story about Cinderella.
    This ensures that the program has some data to work with even if the initial file is missing.

    Parameters:
    - filename (str): The name of the file from which to load the text data.

    Returns:
    - str: The text data loaded from the file or the default text if the file was not found.
    """
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("Text data file not found. Creating a new one with default text.")
        default_text = """Once upon a time, there was a beautiful princess named Cinderella. She lived with her 
        wicked stepmother and stepsisters, who treated her very badly. One day, they received an invitation to a 
        grand ball at the palace. Cinderella's stepmother and stepsisters went to the ball, leaving her behind. 
        Cinderella was sad, but her fairy godmother appeared and transformed her rags into a beautiful gown. She also 
        gave her a pair of glass slippers and a pumpkin carriage. Cinderella went to the ball and danced with the 
        prince, but she had to leave before midnight. As she fled, one of her glass slippers fell off. The prince 
        found the glass slipper and searched the kingdom for its owner. Eventually, he found Cinderella, 
        and they lived happily ever after."""
        with open(filename, 'w') as file:
            file.write(default_text)
        text = default_text
    return text


# Function to save word frequency data to file
def save_word_frequency(word_frequency, filename):
    with open(filename, 'wb') as file:
        pickle.dump(word_frequency, file)


# Function to analyze text and count word frequency

def analyze_text(text):
    word_frequency = {}
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency


# Function to display word frequency
def display_word_frequency(word_frequency):
    print("Word Frequency:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")


# Main function
def main():
    # Title
    title = "Text Analyzer: Word Frequency"
    display_title(title)

    # Load text data from file or create new file with default text
    filename = "words.data"
    text = load_text(filename)

    # Analyze text and count word frequency
    word_frequency = analyze_text(text)

    # Display word frequency
    display_word_frequency(word_frequency)

    # Save word frequency data to file
    save_word_frequency(word_frequency, filename)


# Execute the main function
if __name__ == "__main__":
    main()
