# dev Nicolas

# import
import pygame

from tamagoatchi.lib.event import EventHandler


# class Button
class Button:
    def __init__(self, screen, action, x, y, width, height, color=(255, 0, 0, 128)):
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)
        self.screen = screen
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)  # (r, g, b, transparency)
        self.screen.blit(self.image, self.rect.topleft)

    @EventHandler.register(pygame.MOUSEBUTTONDOWN)
    def on_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            self.action()

    @EventHandler.register(pygame.MOUSEMOTION)
    def on_hover(self, event):
        x, y = event.pos
        if (x in range(self.rect.x, self.rect.x + self.rect.width)) and (y in range(self.rect.y, self.rect.y + self.rect.height)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

