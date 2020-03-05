# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Characters/Sorcerer.py

from SuperClass.Character import Character
from SuperClass.Mage import Mage 
from random import randint
from SuperClass.GameStatistics import GameStatistics

from Global.GLOBAL_CHARACTERS_VARIABLES import MAGE_INITIAL_LIFE, \
											   MAGE_INITIAL_MANA, \
											   MAGE_ADD_MANA_FOR_LEVEL, \
											   MAGE_ADD_LIFE_FOR_LEVEL, \
											   MAGE_REG_LIFE_EACH_TURN, \
											   MAGE_REG_MANA_EACH_TURN, \
									           MAGE_LIGHT_SPELL_MANA_USED, \
									           MAGE_MEDIUM_SPELL_MANA_USED, \
									           MAGE_STRONG_SPELL_MANA_USED

class Sorcerer(Mage):

	'''
	-- Herance livingBeing

	self.totalLife
	self.currentlyLife

	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	deffunction getLiveBeingTotalLife()
	'''

	'''
	-- Herance Character

	self.characterName
	self.characterVocation

	self.currentlyLevel
	self.currentlyXP
	self.xpToNextLevel

	self.totalMana
	self.currentlyMana

	self.totalCapacity
	self.currentlyCapacity

	self.magicLevel
	self.manaUsedToNextMagicLevel
	self.totalManaUsed

	def getCharacterVocation()
	def getCharacterXPToNextLevel()
	def getCharacterCurrentlyMagicLevel()
	def getCharacterCurrentlyLevel()
	def getCharacterCurrentlyMana()
	def getCharacterCurrentlyLife()
	def getCharacterCurrentlyXP()
	def getCharacterTotalManaUsedToNextLevel()
	def getCharacterXPToNextLevel()
	'''

	'''
	-- Herance Mage

	
	'''

	def __init__(self,
				 livingBeingLife,
				 characterName,
				 characterVocation ):

		# construct mage
		super().__init__( MAGE_INITIAL_LIFE,
						  characterName, 
			              characterVocation )


	def __str__():
		print("Character Name: " + self.getCharacterName())
		print("Vocation: " + self.getCharacterVocation())
		print("Level: ".format(self.getCharacterCurrentlyLevel()))
		print("Magic Level: ".format(self.getCharacterMagicLevel()))
		print("Currently Life: ".format(self.getLivingBeingCurrentlyLife()))
		print("Currently Mana: ".format(self.getCharacterCurrentlyMana()))
		print("Total Capacity: ".format(self.getCharacterCurrentlyCapacity()))
	
	def Status(self):
		print("\t Character Name: " + self.getCharacterName())
		print("\t Vocation: " + self.getCharacterVocation())
		print("\t Level: ".format(self.getCharacterCurrentlyLevel()))
		print("\t Magic Level: ".format(self.getCharacterCurrentlyMagicLevel()))
		print("\t Currently Life: ".format(self.getLivingBeingCurrentlyLife())) 
		print("\t Currently Mana: ".format(self.getMageCurrentlyMana()))
		print("\t Total Capacity: ".format(self.getMageCurrentlyCapacity()))