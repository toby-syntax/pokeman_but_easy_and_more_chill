from ai_action import *

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
    print(f"{Player name} deals {damage} damage to {Enemy name}.")
    return enemyHealth

def enemyDamageCalc(enemyType, playerHealth, enemyAttack):
    damage = enemyAttack
    if enemyType in playerStrength:
        damage /= 2
    elif enemyType in playerWeakness:
        damage *= 2
    playerHealth -= damage
    print(f"{Enemy name} deals {damage} damage to {Player name}.")
    return playerHealth

def playerTurn(inventory, ActivePokeman, enemyType, enemyHealth, pokeman.attack):
    while True:
        move = input('You can choose to "Retreat" or "Attack"').lower()
        if move == 'retreat':
            while True:
                NA = input(f'These are your benched pokemon {inventory}, pick on to swap with you active pokeman.').lower()
                if NA in inventory:
                    inventory.append(ActivePokeman)
                    ActivePokeman = NA
                    inventory.remove(NA)
                    print(f'You swapped your active pokemon with {NA}')
                else:
                    print('Please enter a valid option.')
        elif move == 'Attack':
            return(playerDamageCalc(enemyType, enemyHealth, pokeman.attack))
            break
        else:
            print('Please enter a valid option.')
    
def Combat(inventory, List_of_Enemy_Pokemon):
    while len(List_Of_Pokemon) > 0 and len(List_Of_Enemy_Pokemon) > 0:
        print(playerTurn(inventory, inventory[0], enemyType, enemyHealth, pokeman.attack))
        print(ai_action())
