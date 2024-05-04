# dev Nicolas

# import
import pygame
from clock import Clock
from models.player import Player
import tamagotchi


class GameWindow:
    def __init__(self, width: int, height: int):
        self.window = pygame.display.set_mode((width, height))
        self.clock = Clock("console_game")
        self.player = Player("Michel")

        # init pygame
        self.clock = pygame.time.Clock()
        pygame.font.init()
        pygame.display.set_caption("TamaGOATchi")
    
    def write_in_game_window(self,
                             txt: str,
                             font: str,
                             size: int,
                             color: str,
                             x: float= 0,
                             y: float= 0):
        my_font = pygame.font.SysFont(font, size)
        text = my_font.render(txt, True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        self.window.blit(text, textRect)

    def menu_start(self):
        ...
    
    def setting(self):
        ...
    
    def tamagotchis(self):
        ...
    
    def tamagotchi(self, tamagotchi):
        ...

class Game:
    def __init__(self) -> None:
        self.in_game = False



# set gameWindow and game
gameWindow = GameWindow(1200,720)
game = Game()

# main loop
while game.in_game:
    # pygame.QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.in_game = False

    # fill the screen with a color to wipe away anything from last frame
    gameWindow.menu_start()
    gameWindow.write_in_game_window(txt="TamaGOATchi",
                                    font='Comic Sans MS',
                                    size=100,
                                    color=(95, 106, 106),
                                    x=gameWindow.window.get_width()//2,
                                    y=gameWindow.window.get_height()//2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    gameWindow.clock.tick(30)  # limits FPS


pygame.quit()
