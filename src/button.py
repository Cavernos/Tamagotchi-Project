# dev Nicolas

# import
import pygame


# class Button
class Button:
    def __init__(self, game, obj, action, color=(255, 0, 0, 128)):
        self.action = action
        self.rect = pygame.Rect(obj.x*game.zoom,
                                obj.y*game.zoom,
                                obj.width*game.zoom,
                                obj.height*game.zoom)
        
        self.image = pygame.Surface((obj.width*game.zoom, obj.height*game.zoom), pygame.SRCALPHA)
        self.image.fill(color)  # (r, g, b, transparency)
        game.screen.blit(self.image, self.rect.topleft)

    def do_action(self):
        ...


    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
