from character import Character

def test_character_starts_with_10_hp():
    hero = Character("Hero")
    assert hero.hp == 10

def test_character_dies_at_zero_hp():
    hero = Character("Hero")
    hero.hp = 0
    assert hero.is_alive() == False

def test_attack_reduces_hp_by_1():
    hero = Character("Hero")
    enemy = Character("Enemy")
    hero.attack(enemy)
    assert enemy.hp == 9

def test_level_increases_hp():
    hero = Character("Hero", level=2)
    assert hero.hp == 12

def test_level_increases_damage():
    hero = Character("Hero", level=2)
    enemy = Character("Enemy")
    hero.attack(enemy)
    assert enemy.hp == 7