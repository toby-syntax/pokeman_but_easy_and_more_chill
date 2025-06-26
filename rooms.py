def start():
  print('''You wake up and are forced to fight in a dungeon-style gym, against a PE teacher who smells like coffee and cigarettes.
  What pokeman do you pick to fight his f{enemy_type} list. HINT: (fire > grass > water > fire) (electric > water)

  You can pick 1 Tier 3, 2 Tier 2, and 3 Tier 1 Pokeman. The tiers are displayed next to their names. 
  Fire:
  Charman - 1
  Charmelon  - 1
  Charliz - 2
  Minitails - 1
  Tentales - 2
  Moltrez - 3

  Grass:
  Bulbman - 1
  Poisonivysaur - 1
  Aphrosaur - 2
  Beelsprout - 1
  Weepinbeel - 2
  Victorybeel - 2
  Splatterpie - 1
  Splatterpod - 1
  Splatterfree - 2

  Water:
  Squirtman - 1
  Watertle - 1
  Splashsaur - 2
  Giridos - 3
  Staryee - 1
  Starmee - 2
  Articunee - 3

  Electric:
  Pikachu - 1
  Raichu - 2
  Zapdos - 3

  Normal:
  Pidgeman - 1
  Pideetoo - 2
  Pidgeoot - 2
  
  ''')



t1 = 3
t2 = 2
t3 = 1
if t1 > 0 and t2 > 0 and t3 > 0:
  poke_hold = input(f"What is your choice of pokemon, you have {t1} tier ones left, {t2} tier twos left, and {t3} tier threes left. ")
  


