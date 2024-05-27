# dev Nicolas
import types

# import
import pygame

from tamagoatchi.lib.event import EventHandler, EventManager


# class Button
class Button:
    """
    Class used to define a new button widget
    """
    def __init__(self, screen, action, x, y, width, height, color=(255, 0, 0, 128)):
        """
        Add some property like events, rect forms, etc ...
        """
        self.action = action
        self.color = color
        self.event_manager = EventManager.from_id("Button Manager")
        self.event_manager.register(pygame.MOUSEBUTTONDOWN, self.on_click)
        self.event_manager.register(pygame.MOUSEMOTION, self.on_hover)
        self.rect = pygame.Rect(x, y, width, height)
        self.screen = screen
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(self.color)  # (r, g, b, transparency)
        self.screen.blit(self.image, self.rect.topleft)

    def on_click(self, event):
        """
        Define on_click event action
        """
        if self.rect.collidepoint(event.pos):
            self.action(event)
        return

    def on_hover(self, event):
        """
        Define action when mouse hover button
        """
        pos = event.pos
        if self.rect.collidepoint(pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if (pos[0] not in range(self.rect.x, self.rect.x + self.rect.width)
                and pos[1] not in range(self.rect.y, self.rect.y + self.rect.height)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        return

    def destroy(self):
        """
        destroy buttons
        """
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.event_manager.deregister(pygame.MOUSEMOTION, self.on_hover)
        self.event_manager.deregister(pygame.MOUSEBUTTONDOWN, self.on_click)
