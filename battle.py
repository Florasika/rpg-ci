def duel_2v2(team1, team2):
    """
    team1 et team2 sont des listes de 2 personnages
    Les équipes s'attaquent à tour de rôle jusqu'à ce qu'une équipe soit éliminée
    """
    while any(c.is_alive() for c in team1) and any(c.is_alive() for c in team2):
        # team1 attaque team2
        attackers = [c for c in team1 if c.is_alive()]
        defenders = [c for c in team2 if c.is_alive()]
        for attacker in attackers:
            if defenders:
                attacker.attack(defenders[0])
                if not defenders[0].is_alive():
                    defenders.pop(0)

        # team2 attaque team1
        attackers = [c for c in team2 if c.is_alive()]
        defenders = [c for c in team1 if c.is_alive()]
        for attacker in attackers:
            if defenders:
                attacker.attack(defenders[0])
                if not defenders[0].is_alive():
                    defenders.pop(0)

    if any(c.is_alive() for c in team1):
        return team1
    return team2