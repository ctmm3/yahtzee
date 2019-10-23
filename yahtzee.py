#!/usr/bin/python
# Wednesday, October 16, 2019
# Carter and Noel

"""An easy-to-play console yahtzee game."""

import random
import scoring
from utils import *

# List contains scores of each player. first index is always human, the rest refer to number of NPC's.
scores = []
# List contains the order of players. first is always human, the rest refer to number of NPC's.
order = []


def go():
	"""Main turn logic"""
	current_player = order[0]
	print("Let's begin")
	while True:
		w = who(current_player)
		# You roll or they roll?
		if current_player==0:
			pronoun = "you"
		else:
			pronoun = "they"
		if current_player==0:
			print("It's your turn")
		else:
			print("It's "+w+"'s turn")
		current_roll = roll(5)
		saved_dice = []
		num_rolls = 1
		print(pronoun+" roll 5 dice.")
		print(", ".join([str(i) for i in current_roll]))
		if current_player==0:
			#We should only be able to roll 3 times, max
			while num_rolls<4:
				# We need each roll as a string for display
				items = [str(i) for i in current_roll]
				items.append("reroll all")
				items.append("done")
				result = menu("Choose the dice to keep", items)
				#Optionally allow input such as 2 4 to select dice 2 and 4
				spl = result.split(" ")
				#Convert each item in list to an int for simplified processing
				for i in range(len(spl)):
					spl[i] = int(spl[i])
				reroll = False
				done = False
				if len(items) in spl:
					done = True
					spl.remove(len(items))
				if len(items)-1 in spl:
					reroll = True
					spl.remove(len(items)-1)
				for item in spl:
					saved_dice.append(current_roll[item])
				if reroll:
					if num_rolls == 3:
						print("You can't re-roll any more")
					else:
						print("re-rolling")
						current_roll = roll(5-len(saved_dice))
				if done:
					print("done")
					break
				current_roll = roll(5-len(saved_dice))
				num_rolls += 1
			print(saved_dice)
			turn_score = scoring.usr_scores(saved_dice)
			scores[current_player] += turn_score
			print(str(turn_score)+" "+pluralize("point", turn_score!=1, False))
		else:
			print("I'm doing stuff right now")
		#cycle order
		#If we reach the end of our list of players, wrap around
		index = order.index(current_player)
		if index+1==len(order):
			current_player = order[0]
		else:
			current_player = order[index+1]


if __name__ == "__main__":
	print("Welcome to Yahtzee")
	npcs = input("How many NPC's would you like?")
	if not npcs or not npcs.isnumeric():
		print("Invalid input")
	npcs = int(npcs)
	print("You'll be playing with " + str(npcs) + pluralize(" NPC", npcs!=1) + ". Good luck!")
	print("Let's see who goes first")
	# In yahtzee, players usually roll 5 dice, add them up and obtain an order that way.
	summed_rolls = []
	current = []
	for i in range(npcs + 1):
		# You or NPC?
		name = who(i)
		# Roll or rolls?
		r = pluralize("roll", i != 0, False)
		print(name + " " + r + " 5 dice")
		current = roll(5)
		total = sum(current)
		summed_rolls.append(total)
		print(", ".join([str(i) for i in current]))
	order = turn_order(summed_rolls)
	print("the turn order is as follows")
	print(", ".join([who(i) for i in order]))
	#Initialize the score list with slots
	scores = [0] * len(order)
	go()
