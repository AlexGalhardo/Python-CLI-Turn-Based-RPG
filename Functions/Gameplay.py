# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Gameplay.py

from Functions.Prints import *

from SuperClass.Character import Character
from SuperClass.GameStatistics import GameStatistics

from Functions.Mage_Spells import Mage_Spells
from Functions.Warrior_Spells import Warrior_Spells
from Functions.Player_Action import Player_Action

def Gameplay(Player , Monster):

	while True:

		Player.getCharacterRoundStatus()
		Monster.getMonsterRoundStatus()

		playerAction = Player_Action( Player )

		Round_Status_Print()

		if playerAction == 0: # Spell Canceled
			continue

		else:

			if playerAction == 1: # PLAYER USE NORMAL ATTACK IN MONSTER
				GameStatistics.totalAttacksUsed += 1
				damageToMonster = Player.getNormalAttack()
				GameStatistics.totalDamageToMonsters += damageToMonster
				Monster.takeDamage(damageToMonster)

			elif playerAction == 2: # PLAYER USE HEALTH POTION TO REGENERATE LIFE
				Player.useHealthPotion()

			elif playerAction == 3: # PLAYER USE MANA POTION TO REGENERATE Mana
				Player.useManaPotion()

			elif playerAction == 41:
				GameStatistics.totalSpellsUsed += 1
				Monster.takeDamage(Player.useLightSpell())

			elif playerAction == 42:
				GameStatistics.totalSpellsUsed += 1
				Monster.takeDamage(Player.useMediumSpell())

			else:
				GameStatistics.totalSpellsUsed += 1
				Monster.takeDamage(Player.useStrongSpell())


			# MONSTER ROUND --> ATTACK PLAYER
			Player.takeDamage(Monster.Attack())



			# Verify if Player or Monster is Dead
			if Player.isDead():
				# Player still alive? False
				return False
				break

			elif Monster.isDead():

				if Monster.type() == "BOSS":
					return True
					break

				# Player is still alive and monster is dead? True -> next round
				lootMonster = Monster.getMonsterLoot()
				experienceMonster = Monster.getMonsterExperience()

				Player.getLootMonster(lootMonster)
				Player.getMonsterExperience(experienceMonster)

				print('\t Player Looted: {} gold coins.'.format(lootMonster))
				print('\t Player received: {} points of experience!'.format(experienceMonster))
				print('\t Player Currently Experience: {} points experience.'.format(Player.getCharacterCurrentlyXP()))

				Player.Update()

				return True

				break

			else:
				Player.Regenerate()
				# player and monster is still alive
				continue
