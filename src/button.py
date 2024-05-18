# dev Nicolas

# import
import pygame

pygame.init()


# class Button
class Button:
    def __init__(self, screen, action, x, y, width, height, color=(255, 0, 0, 0)):
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)
        
        # Créer une surface avec transparence pour le bouton
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill(color)
        screen.screen.blit(self.image, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
