# Python RPG
# Alex Galhardo Vieira
# https://github.com/AlexGalhardo/Python-RPG
# aleexgvieira@gmail.com
# https://alexgalhardo.com

# !/usr/bin/python3
# coding: utf-8 

# ./Python/SuperClass/Warrior.py

from SuperClass.Character import Character
from random import randint

class Warrior(Character):

	'''
	-- Herance LivingBeing

	protected $totalLife
	protected $currentlyLife
	public function setLiveBeingTotalLife( $setLiveBeingTotalLife )
	public function getLiveBeingTotalLife():int
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

	def __init__( self,
				  livingBeingLife,
				  characterName,
				  warriorWeaponAttack):

		# construct abstract class character
		super().__init__( livingBeingLife, 
		                  characterName,
		                  'Warrior') 

		self.warriorWeaponAttack = warriorWeaponAttack

		self.warriorWeaponSkillLevel = 1

		self.warriorTotalAttacks = 0

		self.warriorTotalAttacksToNextWeaponSkillLevel = 3

		self.warriorDefense = 10

		self.characterVocationType = "WARRIOR"

	
	def getCharacterVocationType(self):
		return self.characterVocationType

	def getWarriorTotalAttacks(self):
		return self.warriorTotalAttacks

	def getWarriorWeaponAttack(self):
		return self.warriorWeaponAttack
	
	def getWarriorTotalAttacksToNextWeaponSkillLevel(self):
		return self.warriorTotalAttacksToNextWeaponSkillLevel

	def getWarriorWeaponSkillLevel(self):
		return self.warriorWeaponSkillLevel

	def getWarriorStatus(self):
		print("\t Character Name: " + self.getCharacterName())
		print("\t Vocation: " + self.getCharacterVocation())
		print("\t Level: {}".format(self.getCharacterCurrentlyLevel()))
		print("\t Magic Level: {}".format(self.getCharacterCurrentlyMagicLevel()))
		print('\t Weapon Skill Level: {}'.format(self.getWarriorWeaponSkillLevel()))
		print("\t Currently Life: {}".format(self.getLivingBeingCurrentlyLife())) 
		print("\t Currently Mana: {}".format(self.getCharacterCurrentlyMana()))

	def getNormalAttack(self):

		print('\t Player attacked the monster.')

		baseAttackOne = int(self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack() * 0.5)
		baseAttackTwo = int(self.getWarriorWeaponSkillLevel() * self.getWarriorWeaponAttack() * 1.5)
		normalAttackDamage = randint(baseAttackOne, baseAttackTwo)
		
		print('\t Normal attack damage: {}'.format(normalAttackDamage))
		
		self.warriorTotalAttacks += 1

		# update weapon skill level
		if( self.getWarriorTotalAttacks() >= self.getWarriorTotalAttacksToNextWeaponSkillLevel() ):
			self.warriorWeaponSkillLevel += 1
			print('\n\t ...Weapon Skill Level UPED!')
			print('\t Currently Weapon Skill Level: {}'.format(self.getWarriorWeaponSkillLevel()))
			self.warriorTotalAttacksToNextWeaponSkillLevel *= 2
			print('\t Currently total attacks: {}'.format(self.getWarriorTotalAttacks()))
			print('\t Total Attacks to next Weapon Skill Level: {}\n'.format(self.getWarriorTotalAttacksToNextWeaponSkillLevel()))


		return normalAttackDamage
	
