# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Monsters/PitsOfInferno_Monsters/Cyclops.py

from SuperClass.NormalMonster import NormalMonster

from Global.GLOBAL_PITS_OF_INFERNO_VARIABLES  import GLOBAL_CYCLOPS_LIFE, \
													GLOBAL_CYCLOPS_NAME, \
										  			GLOBAL_CYCLOPS_WEAPON_ATTACK, \
										  			GLOBAL_CYCLOPS_EXPERIENCE

class Cyclops(NormalMonster):

	'''
	-- Herance LivingBeing

	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	-- Herance NormalMonster

	self.normalMonsterSpellDamage = normalMonsterSpellDamage
	self.normalMonsterName = normalMonsterName
	self.normalMonsterExperienceForKill = normalMonsterExperienceForKill
	self.lootGoldCoins = randint(100, 500)
	'''

	def __init__(self):

		# constructor Normal Monster
		super().__init__( 	GLOBAL_CYCLOPS_LIFE,
							GLOBAL_CYCLOPS_NAME,
							GLOBAL_CYCLOPS_WEAPON_ATTACK,
							GLOBAL_CYCLOPS_EXPERIENCE )

