import random

class Character:
    def __init__(self, name, endurance=0, level=1, force=0, armor=0):
        self.name = name
        self.endurance = endurance
        self.level = level
        self.force = force
        self.armor = armor  # réduit les dégâts reçus
        self.hp = 10 + endurance + (level - 1) * 2

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        D = 1 + self.force + (self.level - 1) * 2
        damage = random.randint(0, D)
        actual_damage = max(0, damage - other.armor)
        other.hp -= actual_damage