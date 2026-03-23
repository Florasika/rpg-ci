import random

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
<<<<<<< Updated upstream
        D = 1
=======
        D = 1 + self.force + (self.level - 1) * 2
>>>>>>> Stashed changes
        damage = random.randint(0, D)
        other.hp -= damage