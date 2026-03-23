class Character:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.hp = 10 + (level - 1) * 2

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        damage = 1 + (self.level - 1) * 2
        other.hp -= damage