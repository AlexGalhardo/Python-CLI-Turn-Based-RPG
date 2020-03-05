# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/Select_Area.py

from Areas.PitsOfInferno_Area import Pits_Of_Inferno_Start_Gameplay

def Select_Area():

	while True:

		print('\n\t --- Chose a area to play ---')
		print('\n\t Enter [1] --> Pits of Inferno --> EASY')
		print('\t Enter [2] --> Inquisition Quest --> MEDIUM')
		print('\t Enter [3] --> Ferumbras Tower --> HARD')
		print('\t Enter [4] --> Play all areas --> Full Game Experience')
		
		areaOption = int(input('\t Area Option: '))

		if areaOption < 1 or areaOption > 4:
			print('\t Choose a valid option!')
			continue
		elif areaOption == 1:
			return 1
			break
		elif areaOption == 2:
			return 2
			break
		elif areaOption == 3:
			return 3
			break
		else:
			return 4
			break

def Adventure_Game_Start( selectedArea, Player ):

	if selectedArea == 1:
		Pits_Of_Inferno_Start_Gameplay( Player )

	elif selectedArea == 2:
		Game_Of_Thrones_Start_Gameplay( Player )

	elif selectedArea == 3:
		Star_Wars_Start_Gameplay( Player )
	
	else:
		Full_Game_Start( Player )
