import os
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_title(title):
    clear_screen()
    print(Fore.YELLOW + "=" * len(title))
    print(Fore.YELLOW + title)
    print(Fore.YELLOW + "=" * len(title))
    print()
