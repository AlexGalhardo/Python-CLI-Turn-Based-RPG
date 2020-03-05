# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/SuperClass/LivingBeing.py

class LivingBeing():

	def __init__(self, 
		         livingBeingLife ):

		self.livingBeingTotalLife = livingBeingLife
		self.livingBeingCurrentlyLife = livingBeingLife

	def setLivingBeingTotalLife(self, setLivingBeingTotalLife ):
		self.livingBeingTotalLife = setLivingBeingTotalLife

	def getLivingBeingTotalLife(self):
		return self.livingBeingTotalLife

	def getLivingBeingCurrentlyLife(self):
		return self.livingBeingCurrentlyLife
