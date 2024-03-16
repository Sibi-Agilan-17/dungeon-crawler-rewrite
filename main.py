import pygame

pygame.init()
pygame.display.set_caption('Dungeon Crawler')
pygame.mouse.set_visible(False)

WIN = pygame.display.set_mode((1050, 750))
display = pygame.Surface((525, 375))
clock = pygame.Clock()

FPS = 60


while True:
	display.fill((28, 31, 36))

	WIN.blit(pygame.transform.scale(display, (1050, 750)), (0, 0))
	pygame.display.flip()
