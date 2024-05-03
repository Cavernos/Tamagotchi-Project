# import
import pygame
import player
import tamagotchi


# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
in_game = True

while in_game:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False

    # fill the screen with a color to wipe away anything from last frame
    window.fill("gray")

    # RENDER YOUR GAME HERE
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    
    text = my_font.render('TamaGOATchi', True, "black")
    
    textRect = text.get_rect()
    textRect.center = (window.get_width() // 2, window.get_height()//2)
    
    window.blit(text, textRect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS

pygame.quit()
