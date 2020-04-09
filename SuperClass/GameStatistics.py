# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/SuperClass/GameStatistics.py

class GameStatistics(object):

	# totalGameTimeUntilPlayerDies = 0
	totalDamageToMonsters = 0
	totalDamageTakenFromMonsters = 0
	totalManaUsed = 0
	totalSpellsUsed = 0
	totalAttacksUsed = 0
	totalHealthPotionsUsed = 0
	totalManaPotionsUsed = 0
	totalHealthPotionsBought = 0
	totalManaPotionsBought = 0
	totalGoldCoinsLooted = 0
	totalGoldCoinsUsed = 0

	# @staticmethod
	# def getTotalGameTimeUntilPlayerDies():
		# print('\t Total Game Time Until Player Dies: {}'.format(GameStatistics.totalGameTimeUntilPlayerDies))
	
	@staticmethod
	def getTotalDamageToMonsters():
		print('\t Total Damage To Monsters: {}'.format(GameStatistics.totalDamageToMonsters))

	@staticmethod
	def getTotalDamageTakenFromMonsters():
		print('\t Total Damage Taken From Monsters: {}'.format(GameStatistics.totalDamageToMonsters))

	@staticmethod
	def getTotalManaUsed():
		print('\t Total Mana Used: {}'.format(GameStatistics.totalManaUsed))

	@staticmethod
	def getTotalSpellsUsed():
		print('\t Total Spells Used: {}'.format(GameStatistics.totalSpellsUsed))

	@staticmethod
	def getTotalAttacksUsed():
		print('\t Total Attacks Used: {}'.format(GameStatistics.totalAttacksUsed))

	@staticmethod
	def getTotalHealthPotionsUsed():
		print('\t Total Health Potions Used: {}'.format(GameStatistics.totalHealthPotionsUsed))

	@staticmethod
	def getTotalManaPotionsUsed():
		print('\t Total Mana Potions Used: {}'.format(GameStatistics.totalManaPotionsUsed))

	@staticmethod
	def getTotalHealthPotionsBought():
		print('\t Total Health Potions Bought: {}'.format(GameStatistics.totalHealthPotionsBought))

	@staticmethod
	def getTotalManaPotionsBought():
		print('\t Total Mana Potions Bought: {}'.format(GameStatistics.totalManaPotionsBought))

	@staticmethod
	def getTotalGoldCoinsLooted():
		print('\t Total Gold Coins Looted: {}'.format(GameStatistics.totalGoldCoinsLooted))

	@staticmethod
	def getTotalGoldCoinsUsed():
		print('\t Total Gold Coins Used: {}'.format(GameStatistics.totalGoldCoinsUsed))

	@staticmethod
	def getGameStatistics():
		#GameStatistics.getTotalGameTimeUntilPlayerDies
		print('\n\t --- Game Statistics ---')
		GameStatistics.getTotalDamageToMonsters()
		GameStatistics.getTotalDamageTakenFromMonsters()
		GameStatistics.getTotalManaUsed()
		GameStatistics.getTotalSpellsUsed()
		GameStatistics.getTotalAttacksUsed()
		GameStatistics.getTotalHealthPotionsUsed()
		GameStatistics.getTotalManaPotionsUsed()
		GameStatistics.getTotalHealthPotionsBought()
		GameStatistics.getTotalManaPotionsBought()
		GameStatistics.getTotalGoldCoinsLooted()
		GameStatistics.getTotalGoldCoinsUsed()
		print('\n\n')
