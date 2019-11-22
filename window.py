import sys 
import pygame

#def key_pressed(key):
	#return pygame.key.get_pressed()[key]



white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
x = 400
y = 400

pygame.init()
display_surface = pygame.display.set_mode((x, y))
pygame.display.set_caption("Window test")

''' create a font object. 
1st parameter = font file present in pygame
2nd parameter = size of font
'''
font = pygame.font.Font('freesansbold.ttf', 32)

'''create a text surface object on which text is drawn
'''
text = font.render('Hello', True,  green, blue)

'''create a rectangular object for the text surface object
and centers it at point (x, y)
'''
textRect = text.get_rect()
textRect.center = (100, 100)


while True :
	'''completey fill the surface with solid color
	'''
	display_surface.fill(white)
	
	'''copying the text surface object to the display
	surface at the center coordinate
	'''
	display_surface.blit(text, textRect)
	
	'''draws the surface object on the screen
	'''
	pygame.display.update()




'''while True:
	pygame.event.pump()
	if key_pressed(pygame.K_ESCAPE):
		print("goodbye")
		sys.exit()
'''
