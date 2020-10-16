import pygame

pygame.init()

dim = (600,600)
board = pygame.display.set_mode(dim)
caption = pygame.display.set_caption("Snake Game")
board.fill((255,255,255))

def buttons():
	return pygame.K_a,pygame.K_d,pygame.K_s,pygame.K_w

def returnSnake(snake_c):
	return {600:snake_c > -50,-50:snake_c < 600}