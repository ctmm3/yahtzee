#todo:
	#usr_scores, present categories in respect to excluded items

#!/usr/bin/python
# Wednesday, October 16, 2019
# Carter and Noel

"""An easy-to-play console yahtzee game."""

import random

#Globals used throughout the program
current_player = 0
# List contains scores of each player. first index is always human, the rest refer to number of NPC's.
scores = []
# List contains the order of players. first is always human, the rest refer to number of NPC's.
order = []
#List contains a list of lists
#The child lists are categories, in the form of indexes of categories, already used by each player and/or NPC
#Each category can only be used once
used_categories = []


#General, multi-purpose functions
def pluralize(term, should, apostrophe=True):
	"""Minimalistic function to pluralize a term, if necessary.
	Only adds "s" to term if should is True."""
	if should:
		if apostrophe:
			return term + "'s"
		else:
			return term + "s"
	else:
		return term


def menu(prompt, items):
	"""Constructs and shows a simple commandline menu.
	Returns the user input."""
	for i in range(len(items)):
		print(str(i) + ": " + items[i])
	result = None
	while True:
		result = input(prompt)
		if result:
			break
	return result


def menu_choice(prompt, items):
	"""Constructs and shows a simple commandline menu.
	Returns an int (index of items) that pertains to the user's selection.
	"""
	for i in range(len(items)):
		print(str(i+1) + ": " + items[i])
	result = None
	while True:
		result = input(prompt)
		if not result.isnumeric():
			continue
		result = int(result)
		if result <= len(items):
			break
	return result-1

def roll(dice):
	"""Rolls dice number of 6-sided dice"""
	rolls = []
	for i in range(dice):
		rolls.append(random.randint(1, 6))
	return rolls


def who(i):
	"""Returns the name of an NPC if i>0, otherwise you"""
	if i == 0:
		return "you"
	else:
		return "NPC " + str(i)


def turn_order(rolls):
	"""given a list of roll sums, returns a list of turn order.
	Turn order is in the form of indexes, where 0=player and everything >0 is NPC's"""
	order = []
	while len(order) < len(rolls):
		maximum = max(rolls)
		index = rolls.index(maximum)
		# Remove this maximum from rolls, otherwise every iteration will return the same one
		# I need caffeination
		rolls[index] = -1  # We shouldn't run into it again.
		order.append(index)
	return order

def is_npc(current_player):
	return current_player!=0

def remove_all(lst, item):
	"""Removes every entry in list matching item"""
	for i in list(lst):
		if i == item:
			lst.remove(item)
	return lst

def get_category(name_or_func):
	"""Returns an index of categories referring to the given category name or function.
	This should be used to easily and efficiently locate scoring categories.
	It can convert "fourK" to "Four of a Kind" and viseversa, for example"""
	for i in range(len(categories)):
		if categories[i][0].lower() == name_or_func:
			return i
		if categories[i][1].__name__ == name_or_func:
			return i
		if categories[i][1] == name_or_func:
			return j
	return


#Functions pertaining to scoring according to yahtzee rules

def best_category(lst):
	"""Given a list of dice, returns the best yahtzee scoring category.
	This is only used for NPC's.
	"""
	#Certain rolls take priority
	#Example, chance is really a last ditch option
	if yahtzee(lst):
		return yahtzee
	elif lgst(lst):
		return lgst
	elif smst(lst):
		return smst
	elif fh(lst):
		return fh
	elif fourK(lst):
		return fourK
	elif threeK(lst):
		return threeK
	#The greatest value yielded after iteration
	#We're really just trying to see which function gives the highest value, maximizing points
	maximum = 0
	maximum_function = None
	for func in (ones, twos, threes, fours, fives, sixs):
		result = func(lst)
		if result>maximum:
			maximum = result
			maximum_function = func
	#Hopefully chance won't even need to be used
	if chance(lst)>maximum:
		maximum_function = chance # :(
		return maximum_function

def usr_scores(lst, category_lst):
	"""Handles choosing of categories by the user.
	This includes displaying a menu and calculating score as it pertains to the user's selection.
	"""
	this_turn = 0
	category = menu_choice("How would you like to score these dice?", category_lst)
	category += 1
	used_categories[current_player].append(category-1)

	if category == 1:
		return ones(lst)

	elif category == 2:
		return twos(lst)

	elif category == 3:
		return threes(lst)

	elif category == 4:
		return fours(lst)
	elif category == 5:
		return fives(lst)

	elif category == 6:
		return sixs(lst)

	elif category == 7:
		return threeK(lst)

	elif category == 8:
		return fourK(lst)

	elif category == 9:
		return fh(lst)

	elif category == 10:
		return smst(lst)

	elif category == 11:
		return lgst(lst)

	elif category == 12:
		return chance(lst)

	elif category == 13:
		return yahtzee(lst)


# ----------- Processing their score selection! ---------------------
#these are self explanitory
#Pass a list (lst) containing values of dice and get score returned as an int

def ones(lst):
	this_turn = 0
	for item in lst:
		if item == 1:
			this_turn = this_turn + 1
	return this_turn


def twos(lst):
	this_turn = 0
	for item in lst:
		if item == 2:
			this_turn = this_turn + 2
	return this_turn


def threes(lst):
	this_turn = 0
	for item in lst:
		if item == 3:
			this_turn = this_turn + 3
	return this_turn


def fours(lst):
	this_turn = 0
	for item in lst:
		if item == 4:
			this_turn = this_turn + 4
	return this_turn


def fives(lst):
	this_turn = 0
	for item in lst:
		if item == 5:
			this_turn = this_turn + 5
	return this_turn


def sixs(lst):
	this_turn = 0
	for item in lst:
		if item == 6:
			this_turn = this_turn + 6
	return this_turn


def threeK(lst):
	if lst.count(1) == 3:
		return sum(lst)
	elif lst.count(2) == 3:
		return sum(lst)
	elif lst.count(3) == 3:
		return sum(lst)
	elif lst.count(4) == 3:
		return sum(lst)
	elif lst.count(5) == 3:
		return sum(lst)
	elif lst.count(6) == 3:
		return sum(lst)
	else:
		return 0


def fourK(lst):
	if lst.count(1) == 4:
		return sum(lst)
	elif lst.count(2) == 4:
		return sum(lst)
	elif lst.count(3) == 4:
		return sum(lst)
	elif lst.count(4) == 4:
		return sum(lst)
	elif lst.count(5) == 4:
		return sum(lst)
	elif lst.count(6) == 4:
		return sum(lst)
	else:
		return 0


def fh(lst):
	if lst.count(1) == 3:
		if lst.count(2) == 2:
			return 25
		elif lst.count(3) == 2:
			return 25
		elif lst.count(4) == 2:
			return 25
		elif lst.count(5) == 2:
			return 25
		elif lst.count(6) == 2:
			return 25

	elif lst.count(2) == 3:
		if lst.count(1) == 2:
			return 25
		elif lst.count(3) == 2:
			return 25
		elif lst.count(4) == 2:
			return 25
		elif lst.count(5) == 2:
			return 25
		elif lst.count(6) == 2:
			return 25

	elif lst.count(3) == 3:
		if lst.count(2) == 2:
			return 25
		elif lst.count(1) == 2:
			return 25
		elif lst.count(4) == 2:
			return 25
		elif lst.count(5) == 2:
			return 25
		elif lst.count(6) == 2:
			return 25

	elif lst.count(4) == 3:
		if lst.count(2) == 2:
			return 25
		elif lst.count(3) == 2:
			return 25
		elif lst.count(1) == 2:
			return 25
		elif lst.count(5) == 2:
			return 25
		elif lst.count(6) == 2:
			return 25

	elif lst.count(5) == 3:
		if lst.count(2) == 2:
			return 25
		elif lst.count(3) == 2:
			return 25
		elif lst.count(4) == 2:
			return 25
		elif lst.count(1) == 2:
			return 25
		elif lst.count(6) == 2:
			return 25

	elif lst.count(6) == 3:
		if lst.count(2) == 2:
			return 25
		elif lst.count(3) == 2:
			return 25
		elif lst.count(4) == 2:
			return 25
		elif lst.count(5) == 2:
			return 25
		elif lst.count(1) == 2:
			return 25
	else:
		return 0

def smst(lst):
	counter1 = 1
	while counter1 < 4:
		if (
			lst.count(counter1) >= 1
			and lst.count(counter1 + 1) >= 1
			and lst.count(counter1 + 2) >= 1
			and lst.count(counter1 + 3) >= 1
		):
			return 30
		else:
			counter1 += 1
	return 0

def lgst(lst):
	if (
		lst.count(1) == 1
		and lst.count(2) == 1
		and lst.count(3) == 1
		and lst.count(4) == 1
		and lst.count(5) == 1
	):
		return 40
	elif (
		lst.count(2) == 1
		and lst.count(3) == 1
		and lst.count(4) == 1
		and lst.count(5) == 1
		and lst.count(6) == 1
	):
		return 40
	else:
		return 0

def chance(lst):
	return sum(lst)

def yahtzee(lst):
	if lst.count(1) == 5:
		return 50
	elif lst.count(2) == 5:
		return 50
	elif lst.count(3) == 5:
		return 50
	elif lst.count(4) == 5:
		return 50
	elif lst.count(5) == 5:
		return 50
	elif lst.count(6) == 5:
		return 50
	else:
		return 0
		

def get_category(name_or_func):
	"""Returns an index of categories referring to the given category name or function.
	This should be used to easily and efficiently locate categories.
	It can convert "fourK" to "Four of a Kind" and viseversa, for example"""
	for i in range(len(categories)):
		if categories[i][0].lower() == name_or_func:
			return i
		if categories[i][1].__name__ == name_or_func:
			return i
		if categories[i][1] == name_or_func:
			return i
	return


#tuple containing mapping of possible score categories to their corresponding functions
categories = (
	("One's", ones),
	("Two's", twos),
	("Three's", threes),
	("Four's", fours),
	("Five's", fives),
	("Six's", sixs),
	("Three of a Kind", threeK),
	("Four of a Kind", fourK),
	("Full House", fh),
	("Small Straight", smst),
	("Large Straight", lgst),
	("Chance", chance),
	("Yahtzee!", yahtzee)
)

def go():
	"""Main turn logic"""
	global current_player
	current_player = order[0]
	print("Let's begin")
	while True:
		#Are we dealing with an NPC or player?
		player = who(current_player)
		# You roll or they roll?
		if not is_npc(current_player):
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
				category = best_category(current_roll)
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
		if not is_npc(current_player):
			categories_to_show = []
			for i in range(len(categories)):
				if get_category(categories[i][1]) not in used_categories[current_player]:
					categories_to_show.append(categories[i][0])
			turn_score = usr_scores(saved_dice, categories_to_show)
		scores[current_player] += turn_score
		print(str(turn_score)+" "+pluralize("point", turn_score!=1, False))
		print(" ")
		print("SCORE TOTALS:")
		print(" ")
		print("Your score = ", scores[0])
		for i in range(1, len(scores)):
			print(who(i),"'s Score = ", scores[i])
		print(" ")			
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
	#Initialize the used_categories list with slots
	for i in range(len(order)):
		used_categories.append([])
	go()
