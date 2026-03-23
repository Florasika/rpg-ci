class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 10

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        other.hp -= 1