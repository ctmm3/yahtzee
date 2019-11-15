import sys 
import pygame

def key_pressed(key):
	return pygame.key.get_pressed()[key]

pygame.init()
pygame.display.set_caption("Window test")
pygame.display.set_mode((900,600), 0, 32)
pygame.image.load('background.gif')
while True:
	pygame.event.pump()
	if key_pressed(pygame.K_ESCAPE):
		print("goodbye")
		sys.exit()
