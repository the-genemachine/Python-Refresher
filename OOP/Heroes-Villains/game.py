import pickle
import random
from colorama import Fore
from util import clear_screen, display_title
from character import GoodGuy, BadGuy
from item import Weapon, Armor

SAVE_FILE = 'game_save.pkl'


def save_game(good_guy):
    with open(SAVE_FILE, 'wb') as file:
        pickle.dump(good_guy, file)
    print(Fore.GREEN + "Game saved successfully!")


def load_game():
    try:
        with open(SAVE_FILE, 'rb') as file:
            good_guy = pickle.load(file)
        print(Fore.GREEN + "Game loaded successfully!")
        return good_guy
    except FileNotFoundError:
        print(Fore.RED + "No save file found.")
        return None


def display_menu():
    print(Fore.CYAN + "Menu Options:")
    print("1. Craft Weapon")
    print("2. Craft Armor")
    print("3. Show Inventory")
    print("4. Battle a Bad Guy")
    print("5. Save Game")
    print("6. Load Game")
    print("7. Exit")


def craft_weapon(good_guy):
    display_title("Craft Weapon")
    weapon_name = input("Enter the name of the weapon: ")
    attack_bonus = random.randint(5, 20)
    weapon = Weapon(weapon_name, attack_bonus)
    good_guy.craft_item(weapon)
    print(Fore.GREEN + f"Crafted {weapon_name} with attack bonus of {attack_bonus}")


def craft_armor(good_guy):
    display_title("Craft Armor")
    armor_name = input("Enter the name of the armor: ")
    defense_bonus = random.randint(10, 30)
    armor = Armor(armor_name, defense_bonus)
    good_guy.craft_item(armor)
    print(Fore.GREEN + f"Crafted {armor_name} with defense bonus of {defense_bonus}")


def battle_bad_guy(good_guy):
    display_title("Battle a Bad Guy")
    bad_guy = BadGuy("Bad Guy")
    print(Fore.RED + str(bad_guy))

    while good_guy.is_alive() and bad_guy.is_alive():
        damage = good_guy.attack(bad_guy)
        print(Fore.GREEN + f"{good_guy.name} attacks {bad_guy.name} for {damage} damage")
        if bad_guy.is_alive():
            damage = bad_guy.attack(good_guy)
            print(Fore.RED + f"{bad_guy.name} attacks {good_guy.name} for {damage} damage")

    if good_guy.is_alive():
        print(Fore.GREEN + f"{good_guy.name} wins!")
    else:
        print(Fore.RED + f"{bad_guy.name} wins!")


def main():
    display_title("Heroes vs. Villains: Craft and Conquer")

    good_guy = None
    while not good_guy:
        player_name = input("Enter your character's name: ")
        good_guy = GoodGuy(player_name)

    while True:
        display_menu()
        choice = input(Fore.YELLOW + "Enter your choice (1-7): ")

        if choice == '1':
            craft_weapon(good_guy)
        elif choice == '2':
            craft_armor(good_guy)
        elif choice == '3':
            display_title("Inventory")
            print(Fore.GREEN + f"Inventory: {good_guy.show_inventory()}")
        elif choice == '4':
            battle_bad_guy(good_guy)
        elif choice == '5':
            save_game(good_guy)
        elif choice == '6':
            good_guy = load_game() or good_guy
        elif choice == '7':
            display_title("Exiting Game")
            print(Fore.YELLOW + "Thank you for playing Heroes vs. Villains: Craft and Conquer!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
