class Item:
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, attack_bonus):
        super().__init__(name)
        self.attack_bonus = attack_bonus


class Armor(Item):
    def __init__(self, name, defense_bonus):
        super().__init__(name)
        self.defense_bonus = defense_bonus
