from rooms.py import *
from pokemon.py import *

status_effects = []
inventory = []

def add_pokemon(pokeman):
  inventory.append(pokeman)

print("Welcome to the world of pokemon!!!")
print("")
inventory = start()
inventory = room1(inventory)
