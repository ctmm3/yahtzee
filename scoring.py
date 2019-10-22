#!/usr/bin/python3
# 10/21/2019
# Noel & Carter

"""This module handles processing of scores in accordence with yahtzee rules"""

#Tuple containing possible score categories
categories = (
	"One's",
	"Two's",
	"Three's",
	"Four's",
	"Five's",
	"Six's",
	"Three of a Kind",
	"Four of a Kind",
	"Full House",
	"Small Straight",
	"Large Straight",
	"Chance",
	"Yahtzee!",
)

from utils import *

def usr_scores(lst):
	this_turn = 0
	category = menu_choice("Choose the category you would like to use: ", categories)
	category += 1

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
		elif lst.countt(4) == 2:
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


if __name__ == "__main__":
	rolls = [3, 4, 5, 6, 1]
	rolls.sort()
	print(usr_scores(rolls))
