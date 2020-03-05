# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Start.py

from Functions.Prints import *
from Functions.Character_Creation import *
from Functions.Gameplay import Gameplay
from Functions.Select_Area import *
from Functions.NPC_Round import NPC_Round

from SuperClass.GameStatistics import GameStatistics

def Start():

	'''
	While the player don't enter 0 to stop the game
	continue the game
	'''
	while True:

		'''
		This function call Prints.py inside ./Functions/
		This function say a brief introduction to the game
		'''
		Game_Introduction()

		'''
		This function call Prints.py inside ./Functions/
		This function says how to play the game
		'''
		How_To_Play_Introduction()

		'''
		This function call Character_Creation inside ./Functions/
		This function create the character name
		'''
		characterName = Create_Character_Name()

		'''
		This function call Character_Creation inside ./Functions/
		This function get character vocation
		'''
		vocationOption = Choose_Character_Vocation()

		'''
		This function call Character_Creation inside ./Functions/
		This function get character objet
		'''
		CharacterObject = Create_Character( characterName, vocationOption )

		'''
		This function call Character_Creation inside ./Functions/
		This function get character objet
		'''
		selectedArea = Select_Area()


		'''
		This function call Adventure_Game_Start inside ./Functions/
		This function start main game loop 
		'''
		Adventure_Game_Start( selectedArea, CharacterObject )

		'''
		If Player Dies or Complete the Area
		'''

		'''
		Show Game Statistics So Far
		'''
		
		GameStatistics.getGameStatistics()

		print('\t Would you like to play again?')
		print('\t Enter [1] --> Yes, lets goo')
		print('\t Enter [0] --> No, I am happy with my perfomance today')
		
		playAgain = int(input('\t Option: '))

		if playAgain == 1:
			continue
		else:
			break

	print('\n\n\t Bye Bye. Come Back Later! :D\n\n')

