from rooms.py import *
from pokemon.py import *
from ai_action import ai_inventory

status_effects = []
inventory = []

def add_pokemon(pokeman):
  inventory.append(pokeman)

print("Welcome to the world of pokemon!!!")
print("")
inventory = start()
enemy_inventory = ai_inventory(grass_type, water_type, fire_type)
inventory = room1(inventory, enemy_inventory)
