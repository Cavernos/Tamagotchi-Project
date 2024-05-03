# dev Nicolas

# import
import pygame
import player
import tamagotchi


class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        pygame.font.init()
        pygame.display.set_caption("TamaGOATchi")
    
    def set_background(self, color: str):
        self.window.fill(color)

    def write_in_game_window(self, txt: str, x: float= 0, y: float= 0):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
    
        text = my_font.render(txt, True, "black")
        
        textRect = text.get_rect()
        # textRect.center = (x, y)
        
        self.window.blit(text, textRect)


# set gameWindow
gameWindow = GameWindow(1200,720)
in_game = True


# main loop
while in_game:
    # pygame.QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False

    # fill the screen with a color to wipe away anything from last frame
    gameWindow.set_background("gray")
    gameWindow.write_in_game_window("TamaGOATchi", gameWindow.window.get_width()//2, gameWindow.window.get_height()//2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    gameWindow.clock.tick(30)  # limits FPS


pygame.quit()
