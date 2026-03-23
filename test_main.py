from character import Character
from unittest.mock import patch

def test_character_starts_with_10_hp():
    hero = Character("Hero")
    assert hero.hp == 10

def test_character_dies_at_zero_hp():
    hero = Character("Hero")
    hero.hp = 0
    assert hero.is_alive() == False

def test_endurance_increases_hp():
    hero = Character("Hero", endurance=5)
    assert hero.hp == 15

def test_level_increases_hp():
    hero = Character("Hero", level=2)
    assert hero.hp == 12

def test_level_increases_damage():
    hero = Character("Hero", level=2, force=3)
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=6):
        hero.attack(enemy)
    assert enemy.hp == 4

def test_force_increases_damage():
    hero = Character("Hero", force=3)
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=4):
        hero.attack(enemy)
    assert enemy.hp == 6

def test_zero_force_gives_1_damage():
    hero = Character("Hero", force=0)
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=1):
        hero.attack(enemy)
    assert enemy.hp == 9

def test_attack_damage_is_random():
    hero = Character("Hero")
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=1):
        hero.attack(enemy)
    assert enemy.hp == 9

def test_attack_can_deal_zero_damage():
    hero = Character("Hero")
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=0):
        hero.attack(enemy)
    assert enemy.hp == 10