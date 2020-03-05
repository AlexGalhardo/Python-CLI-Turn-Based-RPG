# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Gameplay/PitsOfIferno_Gameply.py

from Monsters.Bear import Bear
from Monsters.Cyclops import Cyclops
from Monsters.Hunter import Hunter
from Monsters.Dragon import Dragon
from Monsters.Bear import Bear
from Monsters.Infernalist import Infernalist
from Monsters.Warlock import Warlock
from Monsters.Fury import Fury
from Monsters.DarkTorturer import DarkTorturer
from Monsters.Demon import Demon
from Monsters.Morgaroth import Morgaroth

from Functions.Round_Against_Monster import Round_Against_Monster
from Functions.After_Fight import After_Fight
from Functions.Prints import *
from Functions.NPC_Round import NPC_Round
from Functions.Gameplay import Gameplay

def Pits_Of_Inferno_Start_Gameplay(Player):

	playerAlive = True


	NPC_Round(Player)
	Fight_Round_Print()

	while playerAlive:

		playerAlive = Round_Against_Monster(playerAlive, Player, Bear, False)

		if playerAlive: # Alive against bears?

			playerAlive = Round_Against_Monster(playerAlive, Player, Hunter, False)

			if playerAlive: # Alive against hunters?

				playerAlive = Round_Against_Monster(playerAlive, Player, Cyclops, False)

				if playerAlive: # Alive against Cyclops?

					playerAlive = Round_Against_Monster(playerAlive, Player, Dragon, False)

					if playerAlive: # Alive against Dragons?

						playerAlive = Round_Against_Monster(playerAlive, Player, Infernalist, False)

						if playerAlive: # Alive against Infernalists?

							playerAlive = Round_Against_Monster(playerAlive, Player, Warlock, False)

							if playerAlive: # Alive against Warlocks?

								playerAlive = Round_Against_Monster(playerAlive, Player, Fury, False)

								if playerAlive: # Alive against Furys?

									playerAlive = Round_Against_Monster(playerAlive, Player, DarkTorturer, False)

									if playerAlive: # Alive against DarkTorturers?

										playerAlive = Round_Against_Monster(playerAlive, Player, Demon, False)

										if playerAlive: # Alive against Demons? GO BOSS

											playerAlive = Round_Against_Monster(playerAlive, Player, Morgaroth, True)

											if playerAlive:

												print('\n\n\n\t CONGRATULATIONS! \n\n\t YOU WIN THE GAME!\n\n\n')
												break
											else:
												break
										else:
											break
									else:
										break
								else:
									break
							else:
								break
						else:
							break
					else:
						break
				else:
					break
			else:
				break
		else:
			break
