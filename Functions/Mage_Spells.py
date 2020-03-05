# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Mage_Spells.py

def Mage_Spells( Player ):

	while True:

		print('\n\t Enter [1] --> Light Attack Spell [{}'.format(Player.getMageLightSpellManaUsed()) + ']')
		print('\t Enter [2] --> Medium Attack Spell [{}'.format(Player.getMageMediumSpellManaUsed()) + ']')
		print('\t Enter [3] --> Strong Attack Spell [{}'.format(Player.getMageStrongSpellManaUsed()) + ']')
		print('\t Enter [4] --> Medium Healing [{}'.format(Player.getMageMediumHealingManaUsed()) + ']')
		print('\t Enter [5] --> Strong Healing [{}'.format(Player.getMageStrongHealingManaUsed()) + ']')
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
			if Player.getCharacterCurrentlyMana() >= Player.getMageLightSpellManaUsed():
				return 41
				break

			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageLightSpellManaUsed()))
				continue

		# Return MEDIUM SPEEL
		elif spellOption == 2:
			
			if Player.getCharacterCurrentlyMana() >= Player.getMageMediumSpellManaUsed():
				return 42
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageMediumSpellManaUsed()))
				continue

		# Return STRONG SPELL
		elif spellOption == 3:
			if Player.getCharacterCurrentlyMana() >= Player.getMageStrongSpellManaUsed():
				return 43
				break
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageStrongSpellManaUsed()))
				continue
		
		# MAGE USE MEDIUM HEALING
		elif spellOption == 4:
			if Player.getCharacterCurrentlyMana() >= Player.getMediumHealingManaUsed():
				Player.useMediumHealing()
				continue
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageMediumHealingManaUsed()))
				continue

		# MAGE USE MEDIUM HEALING
		else:
			if Player.getCharacterCurrentlyMana() >= Player.getStrongHealingManaUsed():
				Player.useStrongHealing()
				continue
			else:
				print('\n\t Do not have sufficient mana. Need at least {} mana points.\n'.format(Player.getMageStrongHealingManaUsed()))
		break
