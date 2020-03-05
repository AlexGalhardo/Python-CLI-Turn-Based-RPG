# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Character_Creation.py

from Characters.Knight import Knight
from Characters.Paladin import Paladin
from Characters.Druid import Druid
from Characters.Sorcerer import Sorcerer

from Global.GLOBAL_CHARACTERS_VARIABLES import KNIGHT_INITIAL_LIFE, \
											   PALADIN_INITIAL_LIFE, \
											   MAGE_INITIAL_LIFE


# return a string -> character name
def Create_Character_Name():
	
	characterName = str(input('\n\n\t Enter your character name: '))
	return characterName


def Choose_Character_Vocation():

	while True:

		print('\n\t Chose a vocation below: ')
		print('\t Enter [1] --> Knight')
		print('\t Enter [2] --> Paladin')
		print('\t Enter [3] --> Druid')
		print('\t Enter [4] --> Sorcerer')

		vocationOption = int(input('\t Vocation option: '))

		if vocationOption < 1 or vocationOption > 4:
			print('\n\t Choose a valid option!')
			continue
		else:
			break

	if( vocationOption == 1 ):
		return 1 # knight
	elif vocationOption == 2:
		return 2 # paladin
	elif vocationOption == 3:
		return 3 # druid
	elif vocationOption == 4:
		return 4 # sorcerer


def Choose_Knight_Weapon():

	while True:
		print("\n\t Choose a Weapon Below")
		print("\t Enter [1] --> Sword [Attack: 30 | Defefense: 30")
		print("\t Enter [2] --> Axe [Attack: 35 | Defense: 20")
		print("\t Enter [3] --> Club [Attack: 25 | Defense: 35")
		weaponOption = int(input("\t Weapon Option: "))

		if weaponOption < 1 or weaponOption > 3:
			print("\t Choose a valid option!")
			continue
		else:
			break

	if weaponOption == 1:
		#return "Sword"
		return 30
	elif weaponOption == 2:
		#return "Axe"
		return 35
	else:
		#return "Club"
		return 25


def Choose_Paladin_Weapon():

	while True:
		print("\n\t Choose a Weapon Below")
		print("\t Enter [1] --> Crossbow [Attack: 50]")
		print("\t Enter [2] --> Bow [Attack: 40]")
		print('\t Enter [3] --> Spear [Attack 25]')
		weaponOption = int(input("\t Option: "))

		if weaponOption < 1 or weaponOption > 2:
			print("\t Choose a valid option!")
			continue
		else:
			break

	if weaponOption == 1:
		return 50
	elif weaponOption == 2:
		return 40
	else:
		return 25



def Create_Character( characterName, vocationOption ):

	if vocationOption == 1:

		warriorWeaponAttack = Choose_Knight_Weapon()

		Character = Knight( characterName,
			                warriorWeaponAttack )

	elif vocationOption == 2:

		warriorWeaponAttack = Choose_Paladin_Weapon()

		Character = Paladin( characterName,
			                 warriorWeaponAttack )

	elif vocationOption == 3:

		Character = Druid( characterName,
			               "Druid" )

	else:

		Character = Sorcerer( characterName,
			                  "Sorcerer")


	print('\n\t Character Created!')
	print('\n\t --- SHOWING CHARACTER STATUS ---')
	Character.toString()

	return Character
