# dev Nicolas
import types

# import
import pygame

from tamagoatchi.lib.event import EventHandler


# class Button
class Button:
    def __init__(self, screen, action, x, y, width, height, color=(255, 0, 0, 128)):
        self.action = action
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.screen = screen
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)

    def draw(self):
        self.image.fill(self.color)  # (r, g, b, transparency)
        self.screen.blit(self.image, self.rect.topleft)

    @EventHandler.register(pygame.MOUSEBUTTONDOWN)
    def on_clicked(self, event):
        if self.rect.collidepoint(event.pos):
            if isinstance(self.action, types.MethodType) or isinstance(self.action, types.FunctionType):
                self.action()

    @EventHandler.register(pygame.MOUSEMOTION)
    def on_hover(self, event):
        x, y = event.pos
        if (x in range(self.rect.x, self.rect.x + self.rect.width)) and (
                y in range(self.rect.y, self.rect.y + self.rect.height)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    @staticmethod
    def destroy():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        EventHandler.unregister(pygame.MOUSEMOTION)
        EventHandler.unregister(pygame.MOUSEBUTTONDOWN)
