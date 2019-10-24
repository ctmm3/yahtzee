"""
We are going to do things.
Move all logic specific to handling of players into one statement.
Order all NPC logic below.
Keep relevant portions.
Noel codes this part because I don't want to. #TooHard #NotToday
"""

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
		if not is_npc(current_player):
			pronoun = "you"
			print("It's your turn")
		else:
			pronoun = "they"
			print("It's "+w+"'s turn")
		current_roll = roll(5)
		saved_dice = []
		num_rolls = 1
		turn_score = 0
		print(pronoun+" roll 5 dice.")
		print(", ".join([str(i) for i in current_roll]))
		#We should only be able to roll 3 times, max
		while num_rolls<4:
			# We need each roll as a string for display
			items = [str(i) for i in current_roll]
			if not is_npc(current_player):
				items.append("reroll all")
				items.append("done")				
				result = menu("Choose the dice to keep", items)
				#Optionally allow input such as 2 4 to select dice 2 and 4
				spl = result.split(" ")
				#Convert each item in list to an int for simplified processing
				for i in range(len(spl)):
					spl[i] = int(spl[i])
				if len(items)-1 in spl:
					#Done
					print("done")
					break
				elif len(items)-2 in spl:
					#Re-roll
					if num_rolls == 3:
						print("You can't re-roll any more")
					else:
						print("re-rolling")
						current_roll = roll(5-len(saved_dice))
						num_rolls += 1
						continue
				for item in spl:
					saved_dice.append(current_roll[item])
			#else statement to program npc
			else:
				category = scoring.best_category(current_roll)
				name = category.__name__
				print(items)
				if name == "yahtzee":
					print("The computer got a Yahtzee!")
					turn_score = category(current_roll)
					break
				elif name == "lgst":
					print("The computer got a Large Straight.")
					turn_score = category(current_roll)
					break
				elif name == "chance":
					print("The computer chose Chance.")
					turn_score = category(current_roll)
					break				
				elif name == "smst":
					print("The computer got a Small Straight.")
					turn_score = category(current_roll)
					break
				elif name == "fh":
					print("The computer got a Full House.")
					turn_score = category(current_roll)
					break
				elif name == "fourK":
					print("The computer got a Four-of-a-Kind.")
					turn_score = category(current_roll)
					break
				elif name == "threeK":
					print("The computer got a Three-of-a-Kind.")
					turn_score = category(current_roll)
					break
				elif name == "ones":
					num = 1
				elif name == "twos":
					num = 2
				elif name == "threes":
					num = 3	
				elif name == "fours":
					num = 4		
				elif name == "fives":
					num = 5			
				elif name == "sixs":
					num = 6
				for item in current_roll:
					if item == num:
						saved_dice.append(item)
			current_roll = roll(5-len(saved_dice))
			num_rolls += 1
		if not is_npc(current_player):
			turn_score = scoring.usr_scores(saved_dice)
		scores[current_player] += turn_score
		print(str(turn_score)+" "+pluralize("point", turn_score!=1, False))
		#cycle order
		#If we reach the end of our list of players, wrap around
		index = order.index(current_player)
		if index+1==len(order):
			current_player = order[0]
		else:
			current_player = order[index+1]


if __name__ == "__main__":
	print("Welcome to Yahtzee")
	print(" ")
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
