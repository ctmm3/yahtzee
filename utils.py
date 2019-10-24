#!/usr/bin/python
#Tuesday, October 22, 2019
#Carter and Noel

"""Various utilities useful across parts of the application"""

import random

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
	for i in list(lst):
		if i == item:
			lst.remove(item)
	return lst
