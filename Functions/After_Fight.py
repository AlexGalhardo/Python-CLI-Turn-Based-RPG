# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Gameplay/PitsOfIferno_Gameply.py

from Functions.Prints import *
from Functions.NPC_Round import NPC_Round

def After_Fight( Player ):
	Player_Defeated_Monster() # Prints.py function
	NPC_Round( Player ) # NPC_Round.py function
	Fight_Round_Print() # Prints.py function
