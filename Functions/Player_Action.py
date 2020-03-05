# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Player_Action.py

from Functions.Warrior_Spells import Warrior_Spells
from Functions.Mage_Spells import Mage_Spells

def Player_Action(Player):

	while True:

		print('\n\t @ Player Round @')
		print('\t Enter [1] --> Normal Attack')
		print('\t Enter [2] --> Use Health Potion')
		print('\t Enter [3] --> Use Mana Potion')
		print('\t Enter [4] --> Use Spell')
		playerAction = int(input('\t Option: '))

		if playerAction == 1:
			return 1
			break

		elif playerAction == 2:
			return 2
			break

		elif playerAction == 3:
			return 3
			break

		elif playerAction == 4:

			if Player.getCharacterVocationType() == "WARRIOR":
				spellVerification = Warrior_Spells( Player )
			else:
				spellVerification = Mage_Spells( Player )

			return spellVerification

			break

		else:
			print('\t Enter a valid option!')
			continue