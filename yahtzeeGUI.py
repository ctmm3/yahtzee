#!/usr/bin/python3
#Noel Glamann & Carter Temm
#11.22.2019

'''constructing a GUI for the Yahtzee game'''

import yahtzee
import pygame as py

s_width = 1000
s_height = 850

py.display.init()
py.display.set_mode((s_width, s_height))
py.display.set_caption('Yahtzee!')