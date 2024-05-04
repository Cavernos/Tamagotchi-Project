# dev Nicolas

# import
import pygame
import player
import tamagotchi


class GameWindow:
    def __init__(self, width: int, height: int):
        self.window = pygame.display.set_mode((width, height))
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

    def menu_start(self, color: str= (66, 73, 73)):
        self.window.fill(color)
        pygame.draw.line(self.window, (40, 40, 40), (0, 0), (gameWindow.window.get_width(), 0), 20)
        pygame.draw.line(self.window, (40, 40, 40), (gameWindow.window.get_width(), 0), (gameWindow.window.get_width(), gameWindow.window.get_height()), 20)
        pygame.draw.line(self.window, (40, 40, 40), (gameWindow.window.get_width(), gameWindow.window.get_height()), (0, gameWindow.window.get_height()), 20)
        pygame.draw.line(self.window, (40, 40, 40), (0, gameWindow.window.get_height()), (0, 0), 20)
    
    def setting(self):
        ...
    
    def tamagotchis(self):
        ...
    
    def tamagotchi(self, tamagotchi):
        ...

class Game:
    def __init__(self) -> None:
        self.in_game = False

# set gameWindow
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
