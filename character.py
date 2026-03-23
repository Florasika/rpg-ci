class Character:
    def __init__(self, name, force=0):
        self.name = name
        self.force = force
        self.hp = 10

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        damage = 1 + self.force
        other.hp -= damage