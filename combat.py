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
