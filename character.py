import random

class Character:
    def __init__(self, name, endurance=0, level=1, 
                 force=0, armor=0, weapon=None, agility=0):
        self.name = name
        self.endurance = endurance
        self.level = level
        self.force = force
        self.armor = armor
        self.weapon = weapon
        self.agility = agility
        self.max_hp = self._compute_max_hp()
        self.hp = self.max_hp

    # --- HP ---
    def _compute_max_hp(self):
        return 10 + self.endurance + (self.level - 1) * 2

    def is_alive(self):
        return self.hp > 0

    def is_low_hp(self):
        """Retourne True si HP < 30% du max"""
        return self.hp < self.max_hp * 0.3

    # --- Combat ---
    def _compute_damage(self):
        weapon_bonus = self.weapon.bonus_damage if self.weapon else 0
        D = 1 + self.force + (self.level - 1) * 2 + weapon_bonus
        return random.randint(0, D)

    def _apply_damage(self, damage):
        actual = max(0, damage - self.armor)
        self.hp -= actual

    def attack(self, other):
        damage = self._compute_damage()
        other._apply_damage(damage)
        if not other.is_alive():
            self._level_up()

    # --- Progression ---
    def _level_up(self):
        stat = random.choice(['endurance', 'force', 'armor'])
        if stat == 'endurance':
            self.endurance += 1
            self.max_hp += 1
            self.hp += 1
        elif stat == 'force':
            self.force += 1
        elif stat == 'armor':
            self.armor += 1


def get_first_attacker(char1, char2):
    """Retourne celui avec la plus grande agilité"""
    if char1.agility > char2.agility:
        return char1
    elif char2.agility > char1.agility:
        return char2
    return random.choice([char1, char2])