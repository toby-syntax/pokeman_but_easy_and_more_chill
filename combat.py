def combat(playerType):
    if playerType == "Fire":
        playerWeakness = ["Water", "Rock", "Fire"]
        playerStrength = ["Grass"]

    elif playerType == "Water":
        playerWeakness = ["Water", "Grass"]
        playerStrength = ["Fire", "Rock"]

    elif playerType == "Grass":
        playerWeakness = ["Fire", "Grass"]
        playerStrength = ["Water", "Rock"]

    elif playerType == "Rock":
        playerWeakness = []
        playerStrength = ["Fire"]
    
    elif playerType == "Electric":
        playerWeakness = ["Electric", "Grass"]
        playerStrength = ["Water"]


def playerDamageCalc(enemyType, enemyHealth, playerAttack):
    damage = playerAttack
    if enemyType in playerStrength:
        damage *= 2
    elif enemyType in playerWeakness:
        damage /= 2
    enemyHealth -= damage
    print(f"[Player name] deals {damage} damage to [Enemy name].")
    return enemyHealth

def enemyDamageCalc(enemyType, playerHealth, enemyAttack):
    damage = enemyAttack
    if enemyType in playerStrength:
        damage /= 2
    elif enemyType in playerWeakness:
        damage *= 2
    playerHealth -= damage
    print(f"[Enemy name] deals {damage} damage to [Player name].")
    return playerHealth
