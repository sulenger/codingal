import pygame
def main():
    pygame.init()
    screen_width,screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_capption('color changing sprite')
    colors = {
        'red' : pygame.Color('red'),
        'green': pygame.Color('green')
        'blue': pygame.Color('blue')
        'yellow': pygame.Color('yellow')
        'white': pygame.Color('white')
    }
    