# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Monsters/PitsOfInferno_Monsters/Morgaroth.py

from SuperClass.BOSS import BOSS

from Global.GLOBAL_PITS_OF_INFERNO_VARIABLES import GLOBAL_MORGAROTH_LIFE, \
								   		  			GLOBAL_MORGAROTH_NAME, \
								   		  			GLOBAL_MORGAROTH_WEAPON_ATTACK, \
								   		  			GLOBAL_MORGAROTH_MAGIC_ATTACK, \
								   	      			GLOBAL_MORGAROTH_EXPERIENCE

class Morgaroth(BOSS):

	'''
	-- Herance LivingBeing

	self.livingBeingtotalLife
	self.livingBeingCurrentlyLife
	def setLiveBeingTotalLife( $setLiveBeingTotalLife )
	def getLiveBeingTotalLife():int
	'''

	'''
	-- Herance BOSS

	self.bossMonsterName = bossMonsterName
	self.bossMonsterSpellDamage = bossMonsterSpellDamage
	self.bossMonsterAttackDamage = bossMonsterAttackDamage
	self.bossMonsterExperienceForKill = bossMonsterExperienceForKill
	self.bossMonsterLoot = randint(2000, 5000)
	'''

	def __init__(self):

		# constructor Demon Monster
		super().__init__(   GLOBAL_MORGAROTH_LIFE,
							GLOBAL_MORGAROTH_NAME,
							GLOBAL_MORGAROTH_MAGIC_ATTACK,
							GLOBAL_MORGAROTH_WEAPON_ATTACK,
							GLOBAL_MORGAROTH_EXPERIENCE )
