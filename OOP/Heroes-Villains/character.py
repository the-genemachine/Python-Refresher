import random
from item import Weapon, Armor


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack(self, other):
        damage = random.randint(0, self.attack_power)
        other.take_damage(damage)
        return damage

    def __str__(self):
        return f"{self.name} - Health: {self.health}, Attack Power: {self.attack_power}"


class GoodGuy(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=10)
        self.inventory = []

    def craft_item(self, item):
        self.inventory.append(item)
        if isinstance(item, Weapon):
            self.attack_power += item.attack_bonus
        elif isinstance(item, Armor):
            self.health += item.defense_bonus

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if isinstance(item, Weapon):
                    self.attack_power += item.attack_bonus
                elif isinstance(item, Armor):
                    self.health += item.defense_bonus
                self.inventory.remove(item)
                break

    def show_inventory(self):
        return ', '.join([item.name for item in self.inventory]) or "No items"


class BadGuy(Character):
    def __init__(self, name):
        super().__init__(name, health=50, attack_power=5)
