import random
import sys
import pygame
from ui_style import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('MELLSTROY.GAME')

clock = pygame.time.Clock()

#game assets
is_running = True
coins = 0

#fonts
main_font = pygame.font.Font("../assets/fonts/Super_Trend.ttf", 70)

while is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		screen.fill(PURPLE)

		#TITle
		title_message = main_font.render("MELLSTROY.GAME", True, WHITE)
		title_message_rect = title_message.get_rect(center=(SCREEN_W//2, SCREEN_H//10))
		screen.blit(title_message, title_message_rect)


		pygame.display.update()
		clock.tick(60)