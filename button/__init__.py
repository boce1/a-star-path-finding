import pygame
from utils.var_col import *

pygame.font.init()
font = pygame.font.SysFont("Consolas", 15)

class Button:
    def __init__(self, x, y, message, role):
        self.x = x
        self.y = y
        self.message = message
        self.display_message = font.render(message, True, BLACK)
        self.width1 = self.display_message.get_width()
        self.height1 = self.display_message.get_height()
        self.width = self.width1 + BUTTON_GAP
        self.height = self.height1 + BUTTON_GAP
        self.role = role

    def is_mouse_pointing(self, mouse_x, mouse_y):
        if self.x <= mouse_x <= self.x + self.width:
            if self.y <= mouse_y <= self.y + self.height:
                return True
        return False

    def is_clicked(self, mouse_x, mouse_y, event):
        if self.is_mouse_pointing(mouse_x, mouse_y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
        return False

    def animate(self, win, mouse_x, mouse_y, mouse_pressed):
        if self.is_mouse_pointing(mouse_x, mouse_y):
            if mouse_pressed[0]:
                pygame.draw.rect(win, GRAY, (self.x, self.y, self.width, self.height))


    def draw(self, win, mouse_x, mouse_y, mouse_pressed):
        if self.role == "start":
            pygame.draw.rect(win, GREEN, (self.x, self.y, self.width, self.height))
        elif self.role == "end":
            pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(win, WHITE, (self.x, self.y, self.width, self.height))

        self.animate(win, mouse_x, mouse_y, mouse_pressed)
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 1)
        win.blit(self.display_message, (self.x + BUTTON_GAP // 2, self.y + BUTTON_GAP // 2))

