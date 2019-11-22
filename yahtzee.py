#!/usr/bin/python
# Wednesday, October 16, 2019
# Carter and Noel

"""An easy-to-play console yahtzee game."""

import random
import globals as g
from functions import *

# ----------- Processing their score selection! ---------------------
def usr_scores(lst, category_lst):
	"""Handles choosing of categories by the user.
	This includes displaying a menu and calculating score as it pertains to the user's selection.
	"""
	this_turn = 0
	category = menu_choice("How would you like to score these dice?", category_lst)
	category += 1
	index = get_category(category_lst[category-1])
	g.used_categories[g.current_player].append(index)
	return g.categories[index][1](lst)


def go():
	"""Main turn logic"""
	g.current_player = g.order[0]
	print("Let's begin")
	while True:
		#Are we dealing with an NPC or player?
		player = who(g.current_player)
		# You roll or they roll?
		if not is_npc(g.current_player):
			pronoun = "you"
			print("It's your turn")
		else:
			pronoun = "they"
			print("It's "+player+"'s turn")
		current_roll = roll(5)
		current_roll.sort()
		saved_dice = []
		num_rolls = 1
		turn_score = 0
		print(pronoun+" roll 5 dice.")
		print(", ".join([str(i) for i in current_roll]))
		#We should only be able to roll 3 times, max
		while num_rolls<4:
			# We need each roll as a string for display
			items = [str(i) for i in current_roll]
			if not is_npc(g.current_player):
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
					#Remove done and reroll from items before conversion
					items = items[:-1]
					items = items[:-1]
					for i in range(len(items)):
						items[i] = int(items[i])
					saved_dice += list(items)
					print("done", saved_dice)
					break
				elif len(items)-2 in spl:
					#Re-roll
					if num_rolls == 3:
						print("You can't re-roll any more")
						continue
					else:
						print("re-rolling")
						current_roll = roll(5-len(saved_dice))
						num_rolls += 1
						continue
				for item in spl:
					saved_dice.append(current_roll[item])
			#else statement to program npc
			else:
				categories_to_show = []
				for name, func in g.categories:
					if get_category(name) not in g.used_categories[g.current_player]:
						print(name)
						categories_to_show.append(name)
				category = best_category(current_roll, categories_to_show)
				g.used_categories.append(get_category(category))
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
					turn_score = category(current_roll)
				elif name == "twos":
					num = 2
					turn_score = category(current_roll)
				elif name == "threes":
					num = 3	
					turn_score = category(current_roll)
				elif name == "fours":
					num = 4	
					turn_score = category(current_roll)
				elif name == "fives":
					num = 5	
					turn_score = category(current_roll)
				elif name == "sixs":
					num = 6
					turn_score = category(current_roll)
				for item in current_roll:
					if item == num:
						saved_dice.append(item)
			current_roll = roll(5-len(saved_dice))
			num_rolls += 1
		categories_to_show = []
		for name, func in g.categories:
			if get_category(name) not in g.used_categories[g.current_player]:
				categories_to_show.append(name)
		if not is_npc(g.current_player):
			
			if len(categories_to_show) >= 1:
				turn_score = usr_scores(saved_dice, categories_to_show)
		g.scores[g.current_player] += turn_score
		print(str(turn_score)+" "+pluralize("point", turn_score!=1, False))
		print(" ")
		print("SCORE TOTALS:")
		print(" ")
		print("Your score = ", g.scores[0])
		for i in range(1, len(g.scores)):
			print(who(i),"'s Score = ", g.scores[i])
		if len(categories_to_show) == 0:
			if winner() == "you":
				print('''     You won!!
			                   Can I get a WOOT WOOT!''')
			else:
				print(''' Aw, big fat bummer!
				        The computer won...
					               better luck next time!''')
			break
		print(" ")			
		#cycle order
		#If we reach the end of our list of players, wrap around
		index = g.order.index(g.current_player)
		if index+1==len(g.order):
			g.current_player = g.order[0]
		else:
			g.current_player = g.order[index+1]
			


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
	g.order = turn_order(summed_rolls)
	print("the turn order is as follows")
	print(", ".join([who(i) for i in g.order]))
	#Initialize the score list with slots
	g.scores = [0] * len(g.order)
	#Initialize the used_categories list with slots
	for i in range(len(g.order)):
		g.used_categories.append([])
	go()
