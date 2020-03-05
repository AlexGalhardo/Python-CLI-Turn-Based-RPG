# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Round.py

def Warrior_Spells( Player ):

	while True:

		print('\n\t Enter [1] --> Light Spell [{}'.format(Player.getLightSpellManaUsed()) + ']')
		print('\t Enter [2] --> Medium Spell [{}'.format(Player.getMediumSpellManaUsed()) + ']')
		print('\t Enter [3] --> Strong Spell [{}'.format(Player.getStrongSpellManaUsed()) + ']')
		print('\t Enter [0] --> CANCEL')
		spellOption = int(input('\t Spell: '))

		# INVALID OPTION
		if spellOption != 1 and spellOption > 3:
			print('\t Enter a valid option!')
			continue

		# CANCEL SPELL
		elif spellOption == 0:
			return 0
			break

		# Return LIGHT SPEEL
		elif spellOption == 1:
			if Player.getCharacterCurrentlyMana() >= Player.getLightSpellManaUsed():
				return 41
				break

			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getLightSpellManaUsed()))
				continue

		# Return MEDIUM SPEEL
		elif spellOption == 2:
			
			if Player.getCharacterCurrentlyMana() >= Player.getMediumSpellManaUsed():
				return 42
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMediumSpellManaUsed()))
				continue

		# Return STRONG SPEEL
		else:
			if Player.getCharacterCurrentlyMana() >= Player.getStrongSpellManaUsed():
				return 43
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getStrongSpellManaUsed()))
				continue

		break