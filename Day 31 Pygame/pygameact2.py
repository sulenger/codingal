import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and backround image')

backround_image = pygame.transform.scale(pygame.image.load('backround.png').convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))

penguin_iage = pygame
