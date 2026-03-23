from character import Character, get_first_attacker
from battle import duel_2v2, get_target
from weapon import Weapon
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

def test_duel_2v2_returns_winning_team():
    team1 = [Character("Hero1"), Character("Hero2")]
    team2 = [Character("Enemy1"), Character("Enemy2")]
    with patch('character.random.randint', return_value=1):
        winner = duel_2v2(team1, team2)
    assert winner is not None

def test_duel_2v2_loser_is_dead():
    team1 = [Character("Hero1"), Character("Hero2")]
    team2 = [Character("Enemy1"), Character("Enemy2")]
    with patch('character.random.randint', return_value=1):
        winner = duel_2v2(team1, team2)
    loser = team2 if winner == team1 else team1
    assert all(not c.is_alive() for c in loser)

def test_armor_reduces_damage():
    hero = Character("Hero", force=5)
    enemy = Character("Enemy", armor=2)
    with patch('character.random.randint', return_value=5):
        hero.attack(enemy)
    assert enemy.hp == 7

def test_armor_cannot_give_negative_damage():
    hero = Character("Hero")
    enemy = Character("Enemy", armor=10)
    with patch('character.random.randint', return_value=1):
        hero.attack(enemy)
    assert enemy.hp == 10

def test_weapon_increases_damage():
    sword = Weapon("Sword", bonus_damage=3)
    hero = Character("Hero", weapon=sword)
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=4):
        hero.attack(enemy)
    assert enemy.hp == 6

def test_no_weapon_uses_base_damage():
    hero = Character("Hero")
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=1):
        hero.attack(enemy)
    assert enemy.hp == 9

def test_killing_enemy_triggers_levelup():
    hero = Character("Hero", force=10)
    enemy = Character("Enemy")
    enemy.hp = 1
    with patch('character.random.randint', return_value=5):
        with patch('character.random.choice', return_value='force'):
            hero.attack(enemy)
    assert not enemy.is_alive()
    assert hero.force == 11

def test_no_levelup_if_enemy_survives():
    hero = Character("Hero")
    enemy = Character("Enemy")
    with patch('character.random.randint', return_value=0):
        hero.attack(enemy)
    assert hero.force == 0

def test_highest_agility_attacks_first():
    hero = Character("Hero", agility=10)
    enemy = Character("Enemy", agility=2)
    first = get_first_attacker(hero, enemy)
    assert first == hero

def test_equal_agility_is_random():
    hero = Character("Hero", agility=5)
    enemy = Character("Enemy", agility=5)
    with patch('character.random.choice', return_value=hero):
        first = get_first_attacker(hero, enemy)
    assert first == hero

def test_low_hp_character_is_priority_target():
    hero1 = Character("Hero1")
    hero2 = Character("Hero2")
    hero2.hp = 2
    target = get_target([hero1, hero2])
    assert target == hero2

def test_normal_hp_returns_first_alive():
    hero1 = Character("Hero1")
    hero2 = Character("Hero2")
    target = get_target([hero1, hero2])
    assert target == hero1

def test_dead_characters_not_targeted():
    hero1 = Character("Hero1")
    hero1.hp = 0
    hero2 = Character("Hero2")
    target = get_target([hero1, hero2])
    assert target == hero2