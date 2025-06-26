import random

def ai_inventory()

def ai_action(inventory : list, active_pokemon : object):
  temp_pokemon = ''
  max_health = 0
  win = False
  attack = 0
  type = ''
  if active_pokemon.health < active_pokemon.max_health * 0.1:
      for pokemon in inventory:
        if pokemon.health >= max_health:
          max_health = pokemon.health
          temp_pokemon = pokemon
      active_pokemon = temp_pokemon
      if active_pokemon.health == 0: 
        win = True
  else:
    attack = active_pokemon.damage
    type = active_pokemon.type

  return attack, type, active_pokemon, win
