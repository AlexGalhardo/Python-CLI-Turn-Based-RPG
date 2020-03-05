# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Monsters/PitsOfInferno_Monsters/Warlock.py

from SuperClass.MagicMonster import MagicMonster

from Global.GLOBAL_PITS_OF_INFERNO_VARIABLES import   GLOBAL_WARLOCK_LIFE, \
													  GLOBAL_WARLOCK_NAME, \
												      GLOBAL_WARLOCK_MAGIC_ATTACK, \
													  GLOBAL_WARLOCK_EXPERIENCE

class Warlock(MagicMonster):

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
		super().__init__(   GLOBAL_WARLOCK_LIFE,
							GLOBAL_WARLOCK_NAME,
							GLOBAL_WARLOCK_MAGIC_ATTACK,
							GLOBAL_WARLOCK_EXPERIENCE )