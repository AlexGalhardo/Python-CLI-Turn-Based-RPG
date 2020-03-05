# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/SuperClass/Monsters/NormalMonster.py

from SuperClass.LivingBeing import LivingBeing
from random import randint
from SuperClass.GameStatistics import GameStatistics

# abstract class that knights, paladins, druids and sorcerer must inherit
class NormalMonster(LivingBeing):

	'''
	-- Herance LivingBeing

	self.totalLife
	self.currentlyLife
	def setLiveBeingTotalLife(setLiveBeingTotalLife)
	def getLiveBeingTotalLife()
	'''

	def __init__(self,
					livingBeingLife,
					normalMonsterName,
		    		normalMonsterAttackDamage,
				 	normalMonsterExperienceForKill):

		# construct living being
		super().__init__( livingBeingLife )

		self.normalMonsterAttackDamage = normalMonsterAttackDamage
		self.normalMonsterName = normalMonsterName
		self.normalMonsterExperienceForKill = normalMonsterExperienceForKill
		self.normalMonsterLoot = randint(50, 200)

	def setNormalMonsterName(self,  normalMonsterName ):
		self.normalMonsterName = normalMonsterName


	def getNormalMonsterName(self):
		return self.normalMonsterName;


	def setNormalMonsterExperienceForKill(self,  normalMonsterExperienceForKill ):
		self.normalMonsterExperienceForKill = normalMonsterExperienceForKill


	def getNormalMonsterExperienceForKill(self):
		return self.normalMonsterExperienceForKill


	def setNormalMonsterAttackDamage(self, normalMonsterAttackDamage ):
		self.normalMonsterAttackDamage = normalMonsterAttackDamage


	def normalMonsterAttack(self):
		return randint(1, 2) * self.normalMonsterAttackDamage


	def getMonsterRoundStatus(self):
		print('\n\t --- MONSTER STATUS ---')
		print('\t ' + self.getNormalMonsterName() + ' Life: {}'.format(self.getLivingBeingCurrentlyLife()))

	def takeDamage(self, getDamage):
		GameStatistics.totalDamageToMonsters += getDamage
		self.livingBeingCurrentlyLife -= getDamage

	def isDead(self):
		if self.getLivingBeingCurrentlyLife() <= 0:
			return True
		else:
			return False

	def type(self):
		return "NORMAL"

	def Attack(self):
		baseAttackOne = int(self.normalMonsterAttackDamage * 0.5)
		baseAttackTwo = int(self.normalMonsterAttackDamage * 1.5)
		return randint(baseAttackOne, baseAttackTwo)

	def getMonsterExperience(self):
		return self.normalMonsterExperienceForKill

	def getMonsterLoot(self):
		return self.normalMonsterLoot

	