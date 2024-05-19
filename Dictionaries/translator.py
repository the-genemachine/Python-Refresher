"""This program translates words or phrases from English to French using a dictionary where the keys are English
words or phrases and the values are their corresponding translations in French. The user inputs the text to
translate, and the program translates it using the provided dictionary. If a word or phrase is not found in the
dictionary, it remains unchanged in the translated text. The program includes functions to clear the screen and
display a title for better presentation."""

import os


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


# Function to translate words or phrases
def translate(text, dictionary):
    words = text.split()
    translated_text = " ".join(dictionary.get(word, word) for word in words)
    return translated_text


# Main function
def main():
    # Title
    title = "Language Translator"
    display_title(title)

    # English to French dictionary
    english_to_french = {
        "hello": "bonjour",
        "world": "monde",
        "python": "python",
        "is": "est",
        "awesome": "impressionnant"
    }

    # Input text to translate
    text = input("Enter text to translate from English to French: ")

    # Translate the text
    translated_text = translate(text, english_to_french)

    # Display the translated text
    print("Translated text:", translated_text)


# Execute the main function
if __name__ == "__main__":
    main()
