def get_target(enemies):
    """
    Retourne la cible prioritaire parmi les ennemis vivants.
    Priorité aux personnages avec HP < 30% de leur HP max.
    """
    alive = [c for c in enemies if c.is_alive()]
    if not alive:
        return None

    # HP max = 10 + endurance + (level-1)*2
    priority = [c for c in alive
                if c.hp < (10 + c.endurance + (c.level - 1) * 2) * 0.3]

    if priority:
        return priority[0]
    return alive[0]


def duel_2v2(team1, team2):
    while any(c.is_alive() for c in team1) and any(c.is_alive() for c in team2):
        # team1 attaque la cible prioritaire de team2
        for attacker in [c for c in team1 if c.is_alive()]:
            target = get_target(team2)
            if target:
                attacker.attack(target)

        # team2 attaque la cible prioritaire de team1
        for attacker in [c for c in team2 if c.is_alive()]:
            target = get_target(team1)
            if target:
                attacker.attack(target)

    if any(c.is_alive() for c in team1):
        return team1
    return team2