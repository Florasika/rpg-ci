import random

class Character:
    def __init__(self, name, endurance=0, level=1, force=0, 
                 armor=0, weapon=None, agility=0):
        self.name = name
        self.endurance = endurance
        self.level = level
        self.force = force
        self.armor = armor
        self.weapon = weapon
        self.agility = agility
        self.hp = 10 + endurance + (level - 1) * 2

    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        weapon_bonus = self.weapon.bonus_damage if self.weapon else 0
        D = 1 + self.force + (self.level - 1) * 2 + weapon_bonus
        damage = random.randint(0, D)
        actual_damage = max(0, damage - other.armor)
        other.hp -= actual_damage

        # Si l'ennemi meurt, on gagne un point de stat aléatoire
        if not other.is_alive():
            self.level_up()

    def level_up(self):
        stat = random.choice(['endurance', 'force', 'armor'])
        if stat == 'endurance':
            self.endurance += 1
            self.hp += 1
        elif stat == 'force':
            self.force += 1
        elif stat == 'armor':
            self.armor += 1


def get_first_attacker(char1, char2):
    """Retourne celui qui a le plus d'agilité, tirage au sort si égalité"""
    if char1.agility > char2.agility:
        return char1
    elif char2.agility > char1.agility:
        return char2
    else:
        return random.choice([char1, char2])