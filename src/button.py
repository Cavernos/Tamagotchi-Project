# dev Nicolas

# import
import pygame


# class Button
class Button:
    def __init__(self, game, action, x, y, width, height, color=(255, 0, 0, 0)):
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)
        
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)  # (r, g, b, transparency)
        game.screen.blit(self.image, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
