# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/Functions/NPC.py

from SuperClass.GameStatistics import GameStatistics

def NPC_Round( Player ):

	totalPrice = 0
	continueNPC = True

	while continueNPC:

		print('\n\t ---> NPC ROUND <--- ')
		print('\t Currently Gold Coins: {}'.format(Player.getCharacterCurrentlyGoldCoins()))
		print('\t Enter [1] --> Buy Health Potions [50 gold coins EACH]')
		print('\t Enter [2] --> Buy Mana Potions [50 gold coins EACH]')
		print('\t Enter [0] --> ByeBye NPC [NEXT ROUND]')
		npcOption = int(input('\t Option: '))

		while True:

			if npcOption == 1:

				print('\n\t How many Health Potions you want dear ' + Player.getCharacterName() + ' ?')
				print('\t Enter [0] --> Go back.')
				healthPotions = int(input('\t I want to buy: '))

				if healthPotions == 0:
					break


				GameStatistics.totalHealthPotionsBought += healthPotions
				totalPrice = healthPotions * 50
				print('\t Confirm: [{}] Health Potions for [{}] Gold Coins?'.format(healthPotions, totalPrice))
				print('\t Enter [1] --> Yes')
				print('\t Enter Other --> No')
				confirm = int(input('\t Confirm: '))
				if confirm == 1:
					if totalPrice <= Player.getCharacterCurrentlyGoldCoins():
						Player.usedGoldCoinsInNPC( totalPrice )
						Player.addHealthPotions(healthPotions)
						print('\t Currently Cold Coins: {}'.format(Player.getCharacterCurrentlyGoldCoins()))
						print('\t Currently Health Potions: {}'.format(Player.getCharacterCurrentlyHealthPotions()))
						break
					else:
						print('\n\t YOU DONT HAVE SUFFICIENT GOLD COINS!')
						break
				else:
					continue


			elif npcOption == 2:

					print('\n\t How many Mana Potions you want dear ' + Player.getCharacterName() + ' ?')
					print('\t Enter [0] --> Go back.')
					manaPotions = int(input('\t I want to buy: '))

					if manaPotions == 0:
						break

					GameStatistics.totalManaPotionsBought += manaPotions
					totalPrice = manaPotions * 50
					print('\t Confirm: {} for {} gold coins?'.format(manaPotions, totalPrice))
					print('\t Enter [1] --> Yes')
					print('\t Enter Other --> No')
					confirmTransaction = int(input('\t Confirm: '))

					if confirmTransaction == 1:

						if totalPrice <= Player.getCharacterCurrentlyGoldCoins():
							Player.usedGoldCoinsInNPC( totalPrice )
							Player.addManaPotions(manaPotions)
							print('\t Currently Cold Coins: {}'.format(Player.getCharacterCurrentlyGoldCoins()))
							print('\t Currently Mana Potions: {}'.format(Player.getCharacterCurrentlyManaPotions()))
							break
						else:
							print('\n\t YOU DONT HAVE SUFFICIENT GOLD COINS!')
							break
					else:
						continue

			elif npcOption == 0:
				continueNPC = False
				break

			else:
				print('\t Enter a valid option!')
				break
