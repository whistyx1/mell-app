import random
import sys
import pygame
from ui_style import *
import asyncio
import time

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption('MELLSTROY.GAME')

clock = pygame.time.Clock()

#game assets
is_running = True
score_coins = 0
points = 1

#fonts
main_font = pygame.font.Font("../assets/fonts/Super_Trend.ttf", 70)
score_font = pygame.font.Font("../assets/fonts/Super_Trend.ttf", 30)
authors_font = pygame.font.Font("../assets/fonts/BitcountGridSingleInk-VariableFont_CRSV,ELSH,ELXP,SZP1,SZP2,XPN1,XPN2,YPN1,YPN2,slnt,wght.ttf", 20)

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

		#Score label
		score_message = score_font.render(f'Mellstroy coins: {score_coins}', True, WHITE)
		score_message_rect = score_message.get_rect(center=(SCREEN_W//2, SCREEN_H//6))
		screen.blit(score_message, score_message_rect)
			
	#Authors label
		author_message = authors_font.render('by whistyx & sybrery.', True, WHITE)
		author_message_rect = author_message.get_rect(center=(SCREEN_W//1.25, SCREEN_H//1.04))
		screen.blit(author_message, author_message_rect)


		pygame.display.update()
		clock.tick(60)