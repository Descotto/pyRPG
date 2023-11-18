import pygame
from settings import *
from support import import_folder


class Control:
    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        self.buttons = ['up', 'down', 'left', 'right', 'attack', 'magic', 'switch']       

        self.clicked = ''
    # Rect objects for buttons
        self.button_rects = {
            'up': pygame.Rect(100, 600, BTN_WIDTH, BTN_HEIGHT),
            'down': pygame.Rect(100, 700, BTN_WIDTH, BTN_HEIGHT),
            'left': pygame.Rect(45, 650, BTN_WIDTH, BTN_HEIGHT),
            'right': pygame.Rect(155, 650, BTN_WIDTH, BTN_HEIGHT),
            'attack': pygame.Rect(700, 600, BTN_WIDTH, BTN_HEIGHT),
            'magic': pygame.Rect(600, 650, BTN_WIDTH, BTN_HEIGHT),
            'switch': pygame.Rect(400, 700, BTN_WIDTH, BTN_HEIGHT),
        }

   
    def display_controller(self, player):
                for button in self.buttons:
                    full_path = f'./assets/chrono/buttons/{button}/{button}.png'
                    image = pygame.image.load(full_path).convert_alpha()
                    

                    rect = pygame.Rect(0, 0, BTN_WIDTH, BTN_HEIGHT)

                    if button == 'up':
                        rect.topleft = (UP_BTN_X, UP_BTN_Y)
                    elif button == 'down':
                        rect.topleft = (DOWN_BTN_X, DOWN_BTN_Y)
                    elif button == 'left':
                        rect.topleft = (LEFT_BTN_X, LEFT_BTN_Y)
                    elif button == 'right':
                        rect.topleft = (RIGHT_BTN_X, RIGHT_BTN_Y)
                    elif button == 'attack':
                        rect.topleft = (ATTACK_BTN_X, ATTACK_BTN_Y)
                    elif button == 'magic':
                        rect.topleft = (MAGIC_BTN_X, MAGIC_BTN_Y)
                    elif button == 'switch':
                        rect.topleft = (SWITCH_BTN_X, SWITCH_BTN_Y)

                    self.display_surface.blit(image, rect.topleft)

                    # Check for button click
                    mouse_pos = pygame.mouse.get_pos()
                    if rect.collidepoint(mouse_pos):
                        self.clicked = button
                        player.clicked = button
                        
                        
