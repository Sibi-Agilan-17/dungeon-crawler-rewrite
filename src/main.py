#  import random
import sys
import pygame

# constants

FPS = 90
DEBUG = False  # not used # todo: look into this

pygame.init()
pygame.display.set_caption('Dungeon Crawler')
pygame.mouse.set_visible(False)

WIN = pygame.display.set_mode((1050, 750))
display = pygame.Surface((525, 375))
clock = pygame.Clock()


while True:
	display.fill((28, 31, 36))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# Exit silently
			sys.exit(-1)

		elif event.type == pygame.KEYDOWN:
			# Process essential key presses, that does not influence the game
			# and cannot be over ridden by anything else

			if event.key == pygame.K_q:
				# Quit game
				pygame.quit()

			elif event.key == pygame.K_r:
				# reset the game
				# todo: map reset
				...

			elif event.key == pygame.K_z:
				# toggle debug
				# todo: map debug
				...

			# todo: process events

	WIN.blit(pygame.transform.scale(display, (1050, 750)), (0, 0))
	pygame.display.flip()
