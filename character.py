import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        D = 1
        damage = random.randint(0, D)
        other.hp -= damage