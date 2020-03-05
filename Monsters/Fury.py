# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Monsters/PitsOfInferno_Monsters/Fury.py

from SuperClass.DemonMonster import DemonMonster

from Global.GLOBAL_PITS_OF_INFERNO_VARIABLES import   GLOBAL_FURY_LIFE, \
													  GLOBAL_FURY_NAME, \
													  GLOBAL_FURY_WEAPON_ATTACK, \
													  GLOBAL_FURY_MAGIC_ATTACK, \
													  GLOBAL_FURY_EXPERIENCE

class Fury(DemonMonster):

	'''
	-- Herance LivingBeing

	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	-- Herance Demon Monster

	self.magicMonsterSpellDamage = magicMonsterSpellDamage
	self.magicMonsterName = magicMonsterName
	self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
	self.lootGoldCoins = randint(100, 500)
	'''

	def __init__(self):

		# constructor Demon Monster
		super().__init__( GLOBAL_FURY_LIFE,
						  GLOBAL_FURY_NAME,
						  GLOBAL_FURY_MAGIC_ATTACK,
						  GLOBAL_FURY_WEAPON_ATTACK,
					      GLOBAL_FURY_EXPERIENCE )

