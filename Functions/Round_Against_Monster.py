# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Round_Against_Monster.py

from Functions.Gameplay import Gameplay
from Functions.After_Fight import After_Fight

def Round_Against_Monster(playerAlive, Player, monsterClass, bossRound):

	if bossRound:

		newBoss = monsterClass()

		while True:

			print('\n\n\t XXXXXXXXXXXXXXXXXXXXX')
			print('\t .... BOSS FIGHT .... ')
			print('\t XXXXXXXXXXXXXXXXXXXXX')

			print('\n\n\t ......................')
			print('\t ......................')
			print('\t ...HAHAHAHAHAHAHAHAAH!')
			print('\t ......................')
			print('\t ......................')
			print('\t ......I will kill you!')

			playerStillAlive = Gameplay(Player, newBoss)

			if playerStillAlive:
				break
			else:
				print('\n\n\t ... YOU ARE DEAD...')
				print('\n\n\t ... GAME OVER ...\n\n')
				playerAlive = False
				return playerAlive
				break

		return True

	else: 

		newMonsterOne = monsterClass()
		newMonsterTwo = monsterClass()

		while True:

			playerStillAlive = Gameplay(Player, newMonsterOne)

			if playerStillAlive:
				break
			else:
				print('\n\n\t ... YOU ARE DEAD...')
				print('\n\n\t ... GAME OVER ...\n\n')
				playerAlive = False
				return playerAlive
				break

		After_Fight(Player)

		while True:

			playerStillAlive = Gameplay(Player, newMonsterTwo)

			if playerStillAlive:
				break
			else:
				print('\n\n\t ... YOU ARE DEAD...')
				print('\n\n\t ... GAME OVER ...\n\n')
				playerAlive = False
				return playerAlive
				break

		After_Fight(Player)

		return True
