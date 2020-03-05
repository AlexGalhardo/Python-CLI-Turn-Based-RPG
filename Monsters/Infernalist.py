# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Monsters/PitsOfInferno_Monsters/Infernalist.py

from SuperClass.MagicMonster import MagicMonster

from Global.GLOBAL_PITS_OF_INFERNO_VARIABLES import   GLOBAL_INFERNALIST_LIFE, \
													  GLOBAL_INFERNALIST_NAME, \
			                                          GLOBAL_INFERNALIST_MAGIC_ATTACK, \
			                                          GLOBAL_INFERNALIST_EXPERIENCE

class Infernalist(MagicMonster):

	'''
	-- Herance LivingBeing

	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	-- Herance MagicMonster

	self.magicMonsterSpellDamage = magicMonsterSpellDamage
	self.magicMonsterName = magicMonsterName
	self.magicMonsterExperienceForKill = magicMonsterExperienceForKill
	self.lootGoldCoins = randint(100, 500)
	'''

	def __init__(self):

		# constructor Magic Monster
		super().__init__(   GLOBAL_INFERNALIST_LIFE,
							GLOBAL_INFERNALIST_NAME,
							GLOBAL_INFERNALIST_MAGIC_ATTACK,
							GLOBAL_INFERNALIST_EXPERIENCE )
