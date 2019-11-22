#globals.py
#Friday, November 22, 2019
#carter and Noel

"""Contains functions and variables useful in multiple places throughout the program"""

from functions import *

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

#Index of the current player
current_player = 0

# List contains scores of each player. first index is always human, the rest refer to number of NPC's.
scores = []

# List contains the order of players. first is always human, the rest refer to number of NPC's.
order = []

#List contains a list of lists
#The child lists are categories, in the form of names, already used by each player and/or NPC
#Each category can only be used once
used_categories = []
