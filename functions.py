import random
import globals as g

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


def remove_all(lst, item):
	"""Removes every entry in list matching item"""
	for i in list(lst):
		if i == item:
			lst.remove(item)
	return lst

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


def winner():
	"""Returns the name of the player who currently holds the highest score"""
	return who(g.scores.index(max(g.scores)))

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

def get_category(name_or_func):
	"""Returns an index of categories referring to the given category name or function.
	This should be used to easily and efficiently locate scoring categories.
	It can convert "fourK" to "Four of a Kind" and viseversa, for example"""
	for i in range(len(g.categories)):
		if g.categories[i][0] == name_or_func:
			return i
		if g.categories[i][1].__name__ == name_or_func:
			return i
		if g.categories[i][1] == name_or_func:
			return i

def best_category(lst, categories_lst):
	"""Given a list of dice, returns the best yahtzee scoring category.
	This is only used for NPC's.
	"""
	#Certain rolls take priority
	#Example, chance is really a last ditch option
	if yahtzee(lst) and "yahtzee" in categories_lst:
		return yahtzee
	elif lgst(lst) and "Large Straight" in categories_lst:
		return lgst
	elif smst(lst) and "Small Straight" in categories_lst:
		return smst
	elif fh(lst) and "Full House" in categories_lst:
		return fh
	elif fourK(lst) and "Four of a Kind" in categories_lst:
		return fourK
	elif threeK(lst) and "Three of a Kind":
		return threeK
	#The greatest value yielded after iteration
	#We're really just trying to see which function gives the highest value, maximizing points
	maximum = 0
	maximum_function = None
	for func in (ones, twos, threes, fours, fives, sixs):
		print(g.categories[get_category(func)][0])
		if not g.categories[get_category(func)][0] in categories_lst:
			continue
		result = func(lst)
		if result>maximum:
			maximum = result
			maximum_function = func
	#Hopefully chance won't even need to be used
	if chance(lst)>maximum and "Chance" in categories_lst:
		maximum_function = chance # :(
	return maximum_function


#Functions pertaining to scoring according to yahtzee rules
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
		
