# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Monsters/PitsOfInferno_Monsters/Dragon.py

from SuperClass.MagicMonster import MagicMonster

from Global.GLOBAL_PITS_OF_INFERNO_VARIABLES import   GLOBAL_DRAGON_LIFE, \
													  GLOBAL_DRAGON_NAME, \
													  GLOBAL_DRAGON_MAGIC_ATTACK, \
													  GLOBAL_DRAGON_EXPERIENCE


class Dragon(MagicMonster):

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

		# construct MagicMonster
		super().__init__(   GLOBAL_DRAGON_LIFE,
							GLOBAL_DRAGON_NAME,
							GLOBAL_DRAGON_MAGIC_ATTACK,
							GLOBAL_DRAGON_EXPERIENCE )
